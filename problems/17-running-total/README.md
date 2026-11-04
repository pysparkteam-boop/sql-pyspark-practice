# 17. Running Total of Daily Sales

**Level:** Easy · **Topic:** Window functions (running total)

## Task
For each day, show the sales and the running total of sales up to and including that day.

**Return:** `order_date`, `sales`, `running_total`.

## Tables
- `daily_sales`: `order_date` date, `sales` int

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 17-running-total --engine sql --file my_answer.sql
python run.py 17-running-total --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

`SUM(...) OVER (ORDER BY ...)` keeps every row and adds a cumulative column. Spell out the frame so it is explicit.

</details>

<details><summary>Common mistake</summary>

`GROUP BY` collapses the rows; a window keeps them.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Running Total of Daily Sales](https://pyspark.in/challenges/running-total-of-daily-sales/) · PySpark version: [Running Total of Daily Sales (PySpark)](https://pyspark.in/challenges/running-total-of-daily-sales-pyspark/)
