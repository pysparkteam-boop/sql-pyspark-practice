# 22. Quarterly Sales Pivot by Product

**Level:** Medium · **Topic:** Pivoting (CASE WHEN / pivot)

## Task
Pivot sales so each product is one row with a column per quarter (`Q1_sales` ... `Q4_sales`). Quarters without sales show 0, not NULL.

**Return:** `product_id`, `Q1_sales`, `Q2_sales`, `Q3_sales`, `Q4_sales`, sorted by `product_id`.

## Tables
- `sales`: `sales_id` int, `product_id` int, `quarter` string, `amount` decimal(10,2)

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 22-quarterly-pivot --engine sql --file my_answer.sql
python run.py 22-quarterly-pivot --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

Conditional aggregation in SQL; `groupBy().pivot()` in PySpark. Listing the pivot values keeps column order fixed and saves Spark a pass over the data.

</details>

<details><summary>Common mistake</summary>

Forgetting `ELSE 0` / `fillna(0)`, which leaves NULL for quarters without sales.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Quarterly Sales Pivot by Product](https://pyspark.in/challenges/quarterly-sales-pivot-by-product/)
