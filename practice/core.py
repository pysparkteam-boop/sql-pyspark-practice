"""Shared helpers: load a problem's CSV data into DuckDB or Spark, run a solution, compare with expected.csv.

Comparison rules (same idea as the pyspark.in grader for these problems):
- rows are compared as a multiset (row order is not graded);
- numbers compare after rounding to 2 decimals, so 70000, 70000.0 and 70000.0000 are equal;
- empty CSV cells and SQL NULL / Python None are all NULL;
- column names are not compared, only column count and values.
"""
import csv
import importlib.util
import json
import os
from collections import Counter
from decimal import Decimal, InvalidOperation

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROBLEMS = os.path.join(ROOT, "problems")

DUCK_TYPES = {"int": "INTEGER", "bigint": "BIGINT", "smallint": "SMALLINT", "string": "VARCHAR", "date": "DATE",
              "timestamp": "TIMESTAMP", "double": "DOUBLE", "float": "FLOAT", "boolean": "BOOLEAN"}


def problem_dirs():
    return sorted(d for d in os.listdir(PROBLEMS) if os.path.isdir(os.path.join(PROBLEMS, d)) and d[:2].isdigit())


def resolve(problem):
    """Accept '07', '7', '07-hires-per-year' or a path."""
    if os.path.isdir(problem):
        return os.path.abspath(problem)
    for d in problem_dirs():
        if d == problem or d.split("-", 1)[0] == problem.zfill(2):
            return os.path.join(PROBLEMS, d)
    raise SystemExit("Unknown problem: %s (try one of: %s)" % (problem, ", ".join(problem_dirs())))


def schema(pdir):
    with open(os.path.join(pdir, "schema.json"), encoding="utf-8") as f:
        return json.load(f)


def _csv(pdir, table):
    return os.path.join(pdir, "data", table + ".csv").replace("\\", "/")


# ----------------------------------------------------------------------------- DuckDB
def duckdb_connection(pdir):
    import duckdb
    con = duckdb.connect()
    for table, cols in schema(pdir).items():
        coldefs = ", ".join("'%s': '%s'" % (c["name"], c["type"].upper() if c["type"].startswith("decimal") else DUCK_TYPES[c["type"]])
                            for c in cols)
        con.execute("CREATE TABLE %s AS SELECT * FROM read_csv('%s', header=true, columns={%s}, quote='\"', allow_quoted_nulls=false)"
                    % (table, _csv(pdir, table), coldefs))
    return con


def run_sql(pdir, sql_text):
    con = duckdb_connection(pdir)
    res = con.execute(sql_text)
    return [d[0] for d in res.description], res.fetchall()


# ----------------------------------------------------------------------------- Spark
_SPARK = None


def spark_session():
    global _SPARK
    if _SPARK is None:
        from pyspark.sql import SparkSession
        _SPARK = (SparkSession.builder.master("local[1]").appName("sql-pyspark-practice-pack")
                  .config("spark.sql.shuffle.partitions", "1").config("spark.ui.enabled", "false")
                  .config("spark.sql.session.timeZone", "UTC").getOrCreate())
        _SPARK.sparkContext.setLogLevel("ERROR")
    return _SPARK


def spark_tables(pdir):
    spark = spark_session()
    tables = {}
    for table, cols in schema(pdir).items():
        ddl = ", ".join("`%s` %s" % (c["name"], c["type"]) for c in cols)
        df = (spark.read.schema(ddl).option("header", True).option("quote", '"').option("escape", '"')
              .option("mode", "FAILFAST").csv(_csv(pdir, table)))
        tables[table] = df
        df.createOrReplaceTempView(table)  # so spark.sql(...) works too
    return tables


def run_pyspark(pdir, py_path):
    spec = importlib.util.spec_from_file_location("solution_under_test", py_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "solve"):
        raise SystemExit("%s must define solve(t) returning a DataFrame" % py_path)
    df = mod.solve(spark_tables(pdir))
    return df.columns, [tuple(r) for r in df.collect()]


# ----------------------------------------------------------------------------- comparison
def _norm(v):
    if v is None:
        return None
    if hasattr(v, "isoformat"):
        return v.isoformat(sep=" ") if hasattr(v, "hour") else v.isoformat()
    s = str(v).strip()
    if s == "" or s.upper() == "NULL":
        return None
    try:
        d = Decimal(s)
        if d.is_finite():
            return format(d.quantize(Decimal("0.01")), "f")
    except InvalidOperation:
        pass
    return s


def expected(pdir):
    with open(os.path.join(pdir, "expected.csv"), encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    return rows[0], [tuple(r) for r in rows[1:]]


def compare(pdir, rows):
    exp_cols, exp_rows = expected(pdir)
    got = Counter(tuple(_norm(v) for v in r) for r in rows)
    want = Counter(tuple(_norm(v) for v in r) for r in exp_rows)
    if rows and len(rows[0]) != len(exp_cols):
        return False, "expected %d columns (%s), got %d" % (len(exp_cols), ", ".join(exp_cols), len(rows[0]))
    missing, extra = want - got, got - want
    if not missing and not extra:
        return True, "%d rows match" % len(exp_rows)
    msg = []
    if missing:
        msg.append("missing rows: %s" % list(missing.elements())[:5])
    if extra:
        msg.append("unexpected rows: %s" % list(extra.elements())[:5])
    return False, "; ".join(msg)
