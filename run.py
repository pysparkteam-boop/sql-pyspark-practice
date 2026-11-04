"""Check a SQL or PySpark answer against a problem's expected output.

Examples
  python run.py --list
  python run.py 07                                   # run both reference solutions
  python run.py 07 --engine sql --file my.sql        # check your SQL (DuckDB)
  python run.py 07 --engine pyspark --file my.py     # check your PySpark (define solve(t))
  python run.py --all                                # validate every reference solution
"""
import argparse
import os
import sys

from practice import core


def show(cols, rows, limit=20):
    print("  " + " | ".join(cols))
    for r in rows[:limit]:
        print("  " + " | ".join("NULL" if v is None else str(v) for v in r))
    if len(rows) > limit:
        print("  ... (%d rows)" % len(rows))


def check(pdir, engine, path, verbose=True):
    if engine == "sql":
        with open(path, encoding="utf-8") as f:
            cols, rows = core.run_sql(pdir, f.read())
    else:
        cols, rows = core.run_pyspark(pdir, path)
    ok, msg = core.compare(pdir, rows)
    if verbose:
        show(cols, rows)
    print("%s  %-6s %-45s %s" % ("PASS" if ok else "FAIL", engine, os.path.basename(pdir), msg))
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("problem", nargs="?")
    ap.add_argument("--engine", choices=["sql", "pyspark", "both"], default="both")
    ap.add_argument("--file", help="your solution (.sql for sql, .py defining solve(t) for pyspark)")
    ap.add_argument("--all", action="store_true", help="validate all reference solutions")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    if a.list:
        for d in core.problem_dirs():
            print(d)
        return 0
    targets = core.problem_dirs() if a.all else [a.problem]
    if not targets or targets == [None]:
        ap.print_help()
        return 2
    if a.file and (a.all or a.engine == "both"):
        ap.error("--file needs one problem and --engine sql or --engine pyspark")
    ok = True
    for p in targets:
        pdir = core.resolve(p)
        engines = ["sql", "pyspark"] if a.engine == "both" else [a.engine]
        for e in engines:
            path = a.file or os.path.join(pdir, "solution.sql" if e == "sql" else "solution_pyspark.py")
            ok &= check(pdir, e, path, verbose=not a.all)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
