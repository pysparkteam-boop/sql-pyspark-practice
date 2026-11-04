# 08. Orders: List Orders With Customer Names (INNER JOIN)

**Level:** Easy · **Topic:** Joins (INNER)

## Task
List every order with the name of the customer who placed it. Orders without a matching customer are excluded.

**Return:** `order_id`, `order_date`, `customer_name`, sorted by `order_id`.

## Tables
- `customers`: `customer_id` int, `customer_name` string, `status` string, `register_date` date
- `orders`: `order_id` int, `customer_id` int, `order_date` date, `order_amount` decimal(10,2)

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 08-orders-with-customer-names --engine sql --file my_answer.sql
python run.py 08-orders-with-customer-names --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

An INNER JOIN keeps only rows that match on both sides, which is exactly the requirement.

</details>

<details><summary>Common mistake</summary>

Selecting `customer_id` without a table alias: both tables have it, so the reference is ambiguous.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Orders: List Orders With Customer Names (INNER JOIN)](https://pyspark.in/challenges/orders-list-orders-with-customer-names-inner-join/)
