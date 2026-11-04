"""Every reference solution must match expected.csv on both engines, and common wrong answers must be rejected."""
import os
import sys
import textwrap

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from practice import core  # noqa: E402

PROBLEMS = core.problem_dirs()


@pytest.mark.parametrize("problem", PROBLEMS)
def test_reference_sql(problem):
    pdir = core.resolve(problem)
    with open(os.path.join(pdir, "solution.sql"), encoding="utf-8") as f:
        _, rows = core.run_sql(pdir, f.read())
    ok, msg = core.compare(pdir, rows)
    assert ok, msg


@pytest.mark.parametrize("problem", PROBLEMS)
def test_reference_pyspark(problem):
    pdir = core.resolve(problem)
    _, rows = core.run_pyspark(pdir, os.path.join(pdir, "solution_pyspark.py"))
    ok, msg = core.compare(pdir, rows)
    assert ok, msg


@pytest.mark.parametrize("problem", PROBLEMS)
def test_problem_files_complete(problem):
    pdir = core.resolve(problem)
    for name in ("README.md", "schema.json", "expected.csv", "solution.sql", "solution_pyspark.py"):
        assert os.path.isfile(os.path.join(pdir, name)), name
    for table in core.schema(pdir):
        assert os.path.isfile(os.path.join(pdir, "data", table + ".csv")), table


# The "common mistake" in each README must actually produce a wrong answer on the sample data.
WRONG_SQL = {
    "10": "SELECT c.customer_id, c.customer_name, c.city, COUNT(*) FROM customer c LEFT JOIN orders o "
          "ON o.customer_id = c.customer_id GROUP BY 1, 2, 3",                       # COUNT(*) counts the NULL row
    "11": "SELECT e.employee_id, e.first_name, m.first_name FROM employees e JOIN employees m "
          "ON m.employee_id = e.manager_id",                                          # inner self join drops the CEO
    "14": "SELECT salary FROM salaries ORDER BY salary DESC LIMIT 1 OFFSET 1",        # fine here, see test below
    "20": "SELECT department_id, employee_id, first_name, salary FROM (SELECT *, ROW_NUMBER() OVER "
          "(PARTITION BY department_id ORDER BY salary DESC) rn FROM employees) x WHERE rn <= 3",  # cuts a tie
    "02": "SELECT tx_id, customer, TRY_CAST(TRIM(amount) AS DECIMAL(12,2)) FROM transactions",  # cast first
}


@pytest.mark.parametrize("num", ["10", "11", "20", "02"])
def test_common_mistakes_fail(num):
    pdir = core.resolve(num)
    _, rows = core.run_sql(pdir, WRONG_SQL[num])
    ok, _ = core.compare(pdir, rows)
    assert not ok


def test_offset_trap_on_tied_top_salary(tmp_path):
    """LIMIT/OFFSET returns the tied top salary when two people share the maximum; MAX(< MAX) does not."""
    pdir = core.resolve("14")
    con = core.duckdb_connection(pdir)
    con.execute("INSERT INTO salaries VALUES (99, 'Zed', 95000)")  # second person on the top salary
    offset = con.execute(WRONG_SQL["14"]).fetchall()
    with open(os.path.join(pdir, "solution.sql"), encoding="utf-8") as f:
        ref = con.execute(f.read()).fetchall()
    assert offset == [(95000,)] and ref == [(80000,)]


def test_wrong_pyspark_rejected(tmp_path):
    bad = tmp_path / "bad.py"
    bad.write_text(textwrap.dedent("""
        from pyspark.sql import functions as F
        def solve(t):
            # dropDuplicates on two columns merges two different people called Dan
            return t["customers"].dropDuplicates(["customer_name", "email"]).orderBy("customer_id")
    """))
    pdir = core.resolve("21")
    _, rows = core.run_pyspark(pdir, str(bad))
    ok, _ = core.compare(pdir, rows)
    assert not ok


def test_csv_round_trip_keeps_whitespace_and_null():
    pdir = core.resolve("02")
    t = core.spark_tables(pdir)["transactions"]
    vals = {r["tx_id"]: r["amount"] for r in t.collect()}
    assert vals[5] == " 500 " and vals[4] is None
    con = core.duckdb_connection(pdir)
    assert con.execute("SELECT amount FROM transactions WHERE tx_id = 5").fetchone()[0] == " 500 "
    assert con.execute("SELECT amount FROM transactions WHERE tx_id = 4").fetchone()[0] is None
