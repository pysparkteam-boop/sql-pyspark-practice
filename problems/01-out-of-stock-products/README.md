# 01. Find All Products That Are Out of Stock

**Level:** Easy · **Topic:** Filtering

## Task
List every product that is completely sold out (`stock_quantity = 0`).

**Return:** `product_id`, `product_name`, sorted by `product_id`.

## Tables
- `categories`: `category_id` int, `category_name` string
- `order_items`: `item_id` int, `product_id` int, `quantity` int, `unit_price` decimal(10,2), `order_date` date
- `product_reviews`: `review_id` int, `product_id` int, `rating` decimal(3,1)
- `products`: `product_id` int, `product_name` string, `category_id` int, `stock_quantity` int

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 01-out-of-stock-products --engine sql --file my_answer.sql
python run.py 01-out-of-stock-products --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

A plain row filter. Only `products` is needed; the other tables in the dataset are there to tempt you into an unnecessary join.

</details>

<details><summary>Common mistake</summary>

Joining `order_items` first: a sold-out product may have many order rows, which duplicates it in the result.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Find All Products That Are Out of Stock](https://pyspark.in/challenges/find-all-products-that-are-out-of-stock/)
