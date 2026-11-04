# 18. Day-over-Day Change in Sales

**Level:** Easy · **Topic:** Window functions (LAG)

## Task
Show each day's sales next to the previous day's, and the change between them. The first day has NULLs.

**Return:** `order_date`, `sales`, `prev_day_sales`, `dod_change`.

## Tables
- `daily_sales`: `order_date` date, `sales` int

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 18-day-over-day-change --engine sql --file my_answer.sql
python run.py 18-day-over-day-change --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

`LAG(col)` reads the value from the previous row in the window's order.

</details>

<details><summary>Common mistake</summary>

Replacing the first day's NULL with 0, which reports a fake change equal to the whole first day's sales.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Day-over-Day Change in Sales](https://pyspark.in/challenges/day-over-day-change-in-sales/) · PySpark version: [Day-over-Day Change in Sales (PySpark)](https://pyspark.in/challenges/day-over-day-change-in-sales-pyspark/)
