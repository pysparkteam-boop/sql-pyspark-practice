# 04. Find Customers Who Placed More Than 5 Orders (HAVING)

**Level:** Easy · **Topic:** GROUP BY + HAVING

## Task
A customer reaches the VIP tier with more than 5 orders. Return the qualifying customers and their order count.

**Return:** `customer_id`, `customer_name`, `order_count`, sorted by `order_count` descending.

## Tables
- `customers`: `customer_id` int, `customer_name` string, `status` string, `register_date` date
- `orders`: `order_id` int, `customer_id` int, `order_date` date, `order_amount` decimal(10,2)

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 04-customers-more-than-5-orders --engine sql --file my_answer.sql
python run.py 04-customers-more-than-5-orders --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

Join customers to orders, count per customer, then keep counts above 5 with `HAVING`.

</details>

<details><summary>Common mistake</summary>

Using `>= 5`. The rule is strictly more than five.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Find Customers Who Placed More Than 5 Orders (HAVING)](https://pyspark.in/challenges/find-customers-who-placed-more-than-5-orders-having/)
