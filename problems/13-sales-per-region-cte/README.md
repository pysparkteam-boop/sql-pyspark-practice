# 13. Total Sales per Region using CTEs

**Level:** Easy · **Topic:** CTEs

## Task
Total the sales amount per region, using a CTE to name the intermediate result.

**Return:** `region`, `total_sales`, sorted by `total_sales` descending.

## Tables
- `sales`: `sale_id` int, `region` string, `amount` decimal(10,2)

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 13-sales-per-region-cte --engine sql --file my_answer.sql
python run.py 13-sales-per-region-cte --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

A CTE (`WITH ... AS`) is a named subquery. In PySpark the equivalent is simply a DataFrame assigned to a variable.

</details>

<details><summary>Common mistake</summary>

Thinking a CTE is cached or materialised. In most engines it is inlined like a subquery.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Total Sales per Region using CTEs](https://pyspark.in/challenges/total-sales-per-region-using-ctes/)
