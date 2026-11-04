# 05. HR: Average Salary by Department

**Level:** Easy · **Topic:** Aggregation

## Task
Compute the average salary of each department, rounded to 2 decimals.

**Return:** `department`, `avg_salary`, sorted by `avg_salary` descending.

## Tables
- `employees`: `emp_id` int, `name` string, `department` string, `salary` int, `hire_date` date
- `performance`: `perf_id` int, `emp_id` int, `rating` int, `review_date` date

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 05-average-salary-by-department --engine sql --file my_answer.sql
python run.py 05-average-salary-by-department --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

`AVG` per group. Only `employees` is needed; `performance` is unrelated to the question.

</details>

<details><summary>Common mistake</summary>

Joining `performance` first: each employee has several reviews, so the join repeats salaries (the average happens to survive, but a `SUM` would not).

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [HR: Average Salary by Department](https://pyspark.in/challenges/hr-average-salary-by-department/)
