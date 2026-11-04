# 20. Top 3 Highest-Paid Employees in Each Department

**Level:** Medium · **Topic:** Window functions (top N per group)

## Task
Find the three highest earners in each department. A tie at third place includes everyone tied.

**Return:** `department_id`, `employee_id`, `first_name`, `salary`.

## Tables
- `departments`: `department_id` int, `department_name` string
- `employees`: `employee_id` int, `first_name` string, `department_id` int, `salary` int, `hire_date` date, `manager_id` int

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 20-top-3-per-department --engine sql --file my_answer.sql
python run.py 20-top-3-per-department --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

Rank within each department and keep rank <= 3. `RANK` keeps ties at the boundary; `ROW_NUMBER` would cut one of them.

</details>

<details><summary>Common mistake</summary>

Using `ROW_NUMBER` (drops a tied employee) or `LIMIT 3` (top 3 overall, not per department).

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Top 3 Highest-Paid Employees in Each Department](https://pyspark.in/challenges/top-3-highest-paid-employees-in-each-department/)
