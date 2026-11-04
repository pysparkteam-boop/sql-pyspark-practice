# 14. Second Highest Salary

**Level:** Easy · **Topic:** Subqueries / NULL handling

## Task
Return the second highest *distinct* salary as `second_highest_salary`, or NULL if there is none.

**Return:** One row, one column: `second_highest_salary`.

## Tables
- `salaries`: `id` int, `employee` string, `salary` int

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 14-second-highest-salary --engine sql --file my_answer.sql
python run.py 14-second-highest-salary --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

The highest salary below the maximum is the second highest distinct value. `MAX` over zero rows returns NULL, so the no-answer case is handled for free.

</details>

<details><summary>Common mistake</summary>

`ORDER BY salary DESC LIMIT 1 OFFSET 1` returns the duplicate top salary when two people share it, and returns no row (not NULL) when there is no second salary.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Second Highest Salary](https://pyspark.in/challenges/second-highest-salary/)
