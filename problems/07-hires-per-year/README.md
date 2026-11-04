# 07. Count Employees Hired in Each Year

**Level:** Easy · **Topic:** Date functions

## Task
Count how many employees were hired in each calendar year.

**Return:** `hire_year`, `hire_count`, sorted by `hire_year`.

## Tables
- `departments`: `department_id` int, `department_name` string
- `employees`: `employee_id` int, `first_name` string, `department_id` int, `salary` int, `hire_date` date, `manager_id` int

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 07-hires-per-year --engine sql --file my_answer.sql
python run.py 07-hires-per-year --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

`EXTRACT(YEAR FROM ...)` works in DuckDB, MySQL, PostgreSQL and Spark SQL.

</details>

<details><summary>Common mistake</summary>

Grouping by the full `hire_date`, which gives one row per day instead of per year.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Count Employees Hired in Each Year](https://pyspark.in/challenges/count-employees-hired-in-each-year/)
