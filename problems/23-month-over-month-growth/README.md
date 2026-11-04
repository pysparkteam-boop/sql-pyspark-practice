# 23. Month-over-Month Growth Percentage

**Level:** Medium · **Topic:** Window functions (LAG) + percentages

## Task
Show each month's sales, the previous month's sales, and the growth percentage, rounded to 2 decimals. The first month has NULLs.

**Return:** `month_start`, `sales`, `prev_month_sales`, `mom_growth_pct`.

## Tables
- `monthly_sales`: `month_start` date, `sales` int

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 23-month-over-month-growth --engine sql --file my_answer.sql
python run.py 23-month-over-month-growth --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

`LAG` gives the previous month; growth is `(sales - prev) * 100.0 / prev`.

</details>

<details><summary>Common mistake</summary>

Integer division: `(1200 - 1000) / 1000 * 100` is 0 in engines that divide integers. Multiply by `100.0` first.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Month-over-Month Growth Percentage](https://pyspark.in/challenges/month-over-month-growth-percentage/) · PySpark version: [Month-over-Month Growth Percentage (PySpark)](https://pyspark.in/challenges/month-over-month-growth-percentage-pyspark/)
