# 19. 7-Day Moving Average of Sales

**Level:** Medium · **Topic:** Window functions (moving average)

## Task
Smooth daily sales with a 7-day moving average: each row averages itself and the six rows before it, rounded to 2 decimals.

**Return:** `order_date`, `sales`, `moving_avg_7day`.

## Tables
- `daily_traffic`: `order_date` date, `sales` int

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 19-seven-day-moving-average --engine sql --file my_answer.sql
python run.py 19-seven-day-moving-average --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

A `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` frame. The first six rows average however many rows exist.

</details>

<details><summary>Common mistake</summary>

If dates can be missing, a ROWS frame counts rows, not days. Use a RANGE frame over a date (or fill the gaps) when the requirement is calendar days.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [7-Day Moving Average of Sales](https://pyspark.in/challenges/7-day-moving-average-of-sales/) · PySpark version: [7-Day Moving Average of Sales (PySpark)](https://pyspark.in/challenges/7-day-moving-average-of-sales-pyspark/)
