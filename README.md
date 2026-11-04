# SQL + PySpark Practice Pack

23 practice problems that you can solve in **SQL and in PySpark** on your own laptop, with sample data, expected outputs, reference solutions and an answer checker. They are written for data engineering and analytics interview preparation, and to help people moving from SQL to Spark see how the same idea looks in both.

- Every problem ships with CSV data, a schema, the expected output, and a reference solution in SQL and in PySpark.
- `run.py` checks your answer against the expected output. SQL runs on [DuckDB](https://duckdb.org); PySpark runs on a local Spark session. There is no server, account or network call.
- `pytest` validates every reference solution on both engines (see `tests/`).

## Quick start

You need **Python 3.9–3.11**. PySpark also needs **Java 8, 11 or 17** (check with `java -version`); SQL-only practice (`--engine sql`) works without Java.

**Linux / macOS**

```bash
git clone https://github.com/pysparkteam-boop/sql-pyspark-practice.git
cd sql-pyspark-practice
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt          # duckdb, pyspark, pytest
python run.py --list
python run.py 07                         # check both reference solutions for problem 07
```

**Windows (PowerShell)**

```powershell
git clone https://github.com/pysparkteam-boop/sql-pyspark-practice.git
cd sql-pyspark-practice
py -3.11 -m venv .venv; .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py --list
python run.py 07
```

Java, if you don't have it: Ubuntu/Debian `sudo apt install openjdk-17-jre-headless` · macOS `brew install openjdk@17` · Windows: install Eclipse Temurin 17 from adoptium.net.

**Tested so far:** Python 3.9.13 + Java 8 on Windows 10, from a clean virtual environment (`pip install -r requirements.txt`, then `pytest` and `run.py --all`). The GitHub Actions workflow runs Python 3.9, 3.10 and 3.11 with Java 17 on Ubuntu. Python 3.12 isn't supported by the pinned PySpark 3.5 on Windows.

## Solve a problem

1. Open a problem folder and read its `README.md` (task, tables, expected output).
2. Write your answer:
   - SQL: a file with one `SELECT` (tables are already loaded under their CSV names).
   - PySpark: a file with `def solve(t):` that returns a DataFrame; `t` maps table name to DataFrame. The tables are also registered as temp views, so `spark.sql(...)` works.
3. Check it:

```bash
python run.py 07 --engine sql --file my_answer.sql
python run.py 07 --engine pyspark --file my_answer.py
```

Rows are compared as a set (order is not graded), numbers are compared to 2 decimals, and NULLs must match.

## Problems

| # | Problem | Level | Topic | Practise online |
|---|---|---|---|---|
| 01 | [Find All Products That Are Out of Stock](problems/01-out-of-stock-products/) | Easy | Filtering | [SQL](https://pyspark.in/challenges/find-all-products-that-are-out-of-stock/) |
| 02 | [Filter Numeric Values Stored as Strings (SQL)](problems/02-numeric-strings/) | Easy | Filtering / data cleaning | [SQL](https://pyspark.in/challenges/filter-numeric-values-stored-as-strings-sql/) |
| 03 | [Find Duplicate Emails](problems/03-duplicate-emails/) | Easy | GROUP BY + HAVING | [SQL](https://pyspark.in/challenges/find-duplicate-emails/) |
| 04 | [Find Customers Who Placed More Than 5 Orders (HAVING)](problems/04-customers-more-than-5-orders/) | Easy | GROUP BY + HAVING | [SQL](https://pyspark.in/challenges/find-customers-who-placed-more-than-5-orders-having/) |
| 05 | [HR: Average Salary by Department](problems/05-average-salary-by-department/) | Easy | Aggregation | [SQL](https://pyspark.in/challenges/hr-average-salary-by-department/) |
| 06 | [Number of Orders by Each Customer per Month](problems/06-orders-per-customer-per-month/) | Medium | Date functions | [SQL](https://pyspark.in/challenges/number-of-orders-by-each-customer-per-month/) |
| 07 | [Count Employees Hired in Each Year](problems/07-hires-per-year/) | Easy | Date functions | [SQL](https://pyspark.in/challenges/count-employees-hired-in-each-year/) |
| 08 | [Orders: List Orders With Customer Names (INNER JOIN)](problems/08-orders-with-customer-names/) | Easy | Joins (INNER) | [SQL](https://pyspark.in/challenges/orders-list-orders-with-customer-names-inner-join/) |
| 09 | [Customers Who Have Never Placed an Order](problems/09-customers-without-orders/) | Easy | Joins (anti join) | [SQL](https://pyspark.in/challenges/customers-who-have-never-placed-an-order/) |
| 10 | [Count Orders Per Customer Including Zero](problems/10-order-count-including-zero/) | Easy | Joins (LEFT) + COUNT | [SQL](https://pyspark.in/challenges/count-orders-per-customer-including-zero/) |
| 11 | [List Every Employee With Their Manager's Name (Self JOIN)](problems/11-employee-manager-self-join/) | Easy | Joins (self join) | [SQL](https://pyspark.in/challenges/list-every-employee-with-their-manager-s-name-self-join/) |
| 12 | [Find Employees Who Earn More Than Their Department Average](problems/12-above-department-average/) | Medium | Subquery / CTE vs window | [SQL](https://pyspark.in/challenges/find-employees-who-earn-more-than-their-department-average/) |
| 13 | [Total Sales per Region using CTEs](problems/13-sales-per-region-cte/) | Easy | CTEs | [SQL](https://pyspark.in/challenges/total-sales-per-region-using-ctes/) |
| 14 | [Second Highest Salary](problems/14-second-highest-salary/) | Easy | Subqueries / NULL handling | [SQL](https://pyspark.in/challenges/second-highest-salary/) |
| 15 | [ROW_NUMBER: Find the Highest-Paid Employee in Each Department](problems/15-top-earner-per-department/) | Easy | Window functions (ROW_NUMBER) | [SQL](https://pyspark.in/challenges/row-number-find-the-highest-paid-employee-in-each-department/) |
| 16 | [RANK vs DENSE_RANK: See the Difference Side by Side](problems/16-rank-vs-dense-rank/) | Easy | Window functions (RANK, DENSE_RANK) | [SQL](https://pyspark.in/challenges/rank-vs-dense-rank-see-the-difference-side-by-side/) |
| 17 | [Running Total of Daily Sales](problems/17-running-total/) | Easy | Window functions (running total) | [SQL](https://pyspark.in/challenges/running-total-of-daily-sales/) · [PySpark](https://pyspark.in/challenges/running-total-of-daily-sales-pyspark/) |
| 18 | [Day-over-Day Change in Sales](problems/18-day-over-day-change/) | Easy | Window functions (LAG) | [SQL](https://pyspark.in/challenges/day-over-day-change-in-sales/) · [PySpark](https://pyspark.in/challenges/day-over-day-change-in-sales-pyspark/) |
| 19 | [7-Day Moving Average of Sales](problems/19-seven-day-moving-average/) | Medium | Window functions (moving average) | [SQL](https://pyspark.in/challenges/7-day-moving-average-of-sales/) · [PySpark](https://pyspark.in/challenges/7-day-moving-average-of-sales-pyspark/) |
| 20 | [Top 3 Highest-Paid Employees in Each Department](problems/20-top-3-per-department/) | Medium | Window functions (top N per group) | [SQL](https://pyspark.in/challenges/top-3-highest-paid-employees-in-each-department/) |
| 21 | [Remove Duplicate Customer Records](problems/21-remove-duplicate-customers/) | Medium | Deduplication | [SQL](https://pyspark.in/challenges/remove-duplicate-customer-records/) · [PySpark](https://pyspark.in/challenges/remove-duplicate-customer-records-pyspark/) |
| 22 | [Quarterly Sales Pivot by Product](problems/22-quarterly-pivot/) | Medium | Pivoting (CASE WHEN / pivot) | [SQL](https://pyspark.in/challenges/quarterly-sales-pivot-by-product/) |
| 23 | [Month-over-Month Growth Percentage](problems/23-month-over-month-growth/) | Medium | Window functions (LAG) + percentages | [SQL](https://pyspark.in/challenges/month-over-month-growth-percentage/) · [PySpark](https://pyspark.in/challenges/month-over-month-growth-percentage-pyspark/) |

## Dialect notes

The SQL solutions are written for DuckDB and use standard SQL wherever possible; they also run on PostgreSQL and Spark SQL with little or no change. Where MySQL 8 needs different syntax (date truncation, regular expressions), the problem's README shows the MySQL variant. The MySQL variants follow the MySQL 8.0 reference manual but have not yet been executed by the test suite, which runs DuckDB and Spark only.

## Run the tests

```bash
pytest -q              # 76 tests: every reference solution on both engines, plus common-mistake checks
python run.py --all    # 46 reference solutions
```

## SQL vs PySpark examples

`guide/sql_vs_pyspark_examples.py` runs every example from the [SQL vs PySpark guide](https://pyspark.in/learn/sql-vs-pyspark/) on one shared dataset and checks that SQL and PySpark return the same rows:

```bash
python guide/sql_vs_pyspark_examples.py
```

## Licence

- Code (`run.py`, `practice/`, `tests/`, `solution*.{sql,py}`): [MIT](LICENSE).
- Problem text and datasets (`problems/**/README.md`, `data/`, `expected.csv`): [CC BY 4.0](LICENSE-CONTENT.md). Attribution: "SQL + PySpark Practice Pack by PySpark.in".

## About

The problems are adapted from free challenges on [PySpark.in](https://pyspark.in/challenges/), where you can run them in the browser against additional test cases. Disclosure: this pack is maintained by PySpark.in. Everything in this repository is free and works offline.
