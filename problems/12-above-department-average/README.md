# 12. Find Employees Who Earn More Than Their Department Average

**Level:** Medium · **Topic:** Subquery / CTE vs window

## Task
Find employees who earn more than the average salary of their own department.

**Return:** `employee_id`, `first_name`, `salary`, `department_id`, sorted by `salary` descending.

## Tables
- `departments`: `department_id` int, `department_name` string
- `employees`: `employee_id` int, `first_name` string, `department_id` int, `salary` int, `hire_date` date, `manager_id` int

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 12-above-department-average --engine sql --file my_answer.sql
python run.py 12-above-department-average --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

Compute each department's average once (CTE), then compare. The PySpark version shows the window-function alternative: an average over a partition, with no join.

</details>

<details><summary>Common mistake</summary>

Comparing with the company-wide average instead of the department's own average.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Find Employees Who Earn More Than Their Department Average](https://pyspark.in/challenges/find-employees-who-earn-more-than-their-department-average/)
