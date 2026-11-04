# 21. Remove Duplicate Customer Records

**Level:** Medium · **Topic:** Deduplication

## Task
Rows are duplicates only when `customer_name`, `email` and `phone` are all identical. Keep one row per duplicate group, the one with the smallest `customer_id`.

**Return:** `customer_id`, `customer_name`, `email`, `phone`, sorted by `customer_id`.

## Tables
- `customers`: `customer_id` int, `customer_name` string, `email` string, `phone` string

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 21-remove-duplicate-customers --engine sql --file my_answer.sql
python run.py 21-remove-duplicate-customers --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

Number rows inside each duplicate group ordered by id and keep row 1. The partition defines what "the same" means, so all three columns go in it.

</details>

<details><summary>Common mistake</summary>

`dropDuplicates(['customer_name','email'])` merges two different people who share a name and email, and it does not guarantee which id survives.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Remove Duplicate Customer Records](https://pyspark.in/challenges/remove-duplicate-customer-records/) · PySpark version: [Remove Duplicate Customer Records (PySpark)](https://pyspark.in/challenges/remove-duplicate-customer-records-pyspark/)
