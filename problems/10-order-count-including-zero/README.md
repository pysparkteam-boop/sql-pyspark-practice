# 10. Count Orders Per Customer Including Zero

**Level:** Easy · **Topic:** Joins (LEFT) + COUNT

## Task
Report how many orders every customer has placed, showing 0 for customers with none.

**Return:** `customer_id`, `customer_name`, `city`, `order_count`, sorted by `customer_id`.

## Tables
- `customer`: `customer_id` int, `customer_name` string, `city` string
- `orders`: `order_id` int, `customer_id` int, `order_date` date, `amount` decimal(10,2), `aspect` string

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 10-order-count-including-zero --engine sql --file my_answer.sql
python run.py 10-order-count-including-zero --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

LEFT JOIN keeps every customer; `COUNT(o.order_id)` counts only real orders because it ignores NULLs.

</details>

<details><summary>Common mistake</summary>

`COUNT(*)` after a LEFT JOIN counts the NULL row too, so customers without orders show 1 instead of 0.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Count Orders Per Customer Including Zero](https://pyspark.in/challenges/count-orders-per-customer-including-zero/)
