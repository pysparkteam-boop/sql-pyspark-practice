# 15. ROW_NUMBER: Find the Highest-Paid Employee in Each Department

**Level:** Easy · **Topic:** Window functions (ROW_NUMBER)

## Task
Return exactly one row per department: its highest-paid employee. Break salary ties with the lower `emp_id`.

**Return:** `emp_id`, `emp_name`, `department`, `salary`.

## Tables
- `employees_wf`: `emp_id` int, `emp_name` string, `department` string, `salary` int

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 15-top-earner-per-department --engine sql --file my_answer.sql
python run.py 15-top-earner-per-department --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

`ROW_NUMBER()` numbers rows inside each department; the tie-breaker in `ORDER BY` makes the result deterministic.

</details>

<details><summary>Common mistake</summary>

Leaving out the tie-breaker: with two equal top salaries the engine may return either employee, and results change between runs.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [ROW_NUMBER: Find the Highest-Paid Employee in Each Department](https://pyspark.in/challenges/row-number-find-the-highest-paid-employee-in-each-department/)
