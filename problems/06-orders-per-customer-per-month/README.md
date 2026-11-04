# 06. Number of Orders by Each Customer per Month

**Level:** Medium · **Topic:** Date functions

## Task
Count each customer's orders per calendar month, with the month shown as its first day (for example `2024-01-01`).

**Return:** `customer_id`, `month`, `order_count`, sorted by `customer_id`, `month`.

## Tables
- `sales`: `order_id` int, `customer_id` int, `product_id` int, `amount` int, `order_date` date

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 06-orders-per-customer-per-month --engine sql --file my_answer.sql
python run.py 06-orders-per-customer-per-month --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

Truncate the date to the month, then group by customer and month.

</details>

<details><summary>Common mistake</summary>

Grouping by `MONTH(order_date)` alone, which merges January 2024 with January 2025.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

MySQL variant: `DATE_FORMAT(order_date, '%Y-%m-01') AS month   -- MySQL has no DATE_TRUNC`

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Number of Orders by Each Customer per Month](https://pyspark.in/challenges/number-of-orders-by-each-customer-per-month/)
