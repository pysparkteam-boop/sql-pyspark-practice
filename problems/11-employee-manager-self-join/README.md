# 11. List Every Employee With Their Manager's Name (Self JOIN)

**Level:** Easy · **Topic:** Joins (self join)

## Task
Show each employee with their manager's first name. The top manager has no manager, so show NULL for them.

**Return:** `employee_id`, `first_name`, `manager_name`, sorted by `employee_id`.

## Tables
- `departments`: `department_id` int, `department_name` string
- `employees`: `employee_id` int, `first_name` string, `department_id` int, `salary` int, `hire_date` date, `manager_id` int

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 11-employee-manager-self-join --engine sql --file my_answer.sql
python run.py 11-employee-manager-self-join --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

Join `employees` to itself: one copy plays the employee, the other the manager. Use a LEFT JOIN so the top manager is kept.

</details>

<details><summary>Common mistake</summary>

An INNER self join silently drops the employee whose `manager_id` is NULL.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [List Every Employee With Their Manager's Name (Self JOIN)](https://pyspark.in/challenges/list-every-employee-with-their-manager-s-name-self-join/)
