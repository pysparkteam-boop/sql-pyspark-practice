# 09. Customers Who Have Never Placed an Order

**Level:** Easy · **Topic:** Joins (anti join)

## Task
Find the customers who have never placed an order.

**Return:** `customer_id`, `customer_name`, `city`.

## Tables
- `customer`: `customer_id` int, `customer_name` string, `city` string
- `orders`: `order_id` int, `customer_id` int, `order_date` date, `amount` decimal(10,2), `aspect` string

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 09-customers-without-orders --engine sql --file my_answer.sql
python run.py 09-customers-without-orders --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

LEFT JOIN and keep the rows where the right side is NULL. In PySpark the same idea is a `left_anti` join.

</details>

<details><summary>Common mistake</summary>

Using `NOT IN (SELECT customer_id FROM orders)` when `orders.customer_id` can be NULL: one NULL makes `NOT IN` return no rows at all.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Customers Who Have Never Placed an Order](https://pyspark.in/challenges/customers-who-have-never-placed-an-order/)
