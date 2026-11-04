# 03. Find Duplicate Emails

**Level:** Easy · **Topic:** GROUP BY + HAVING

## Task
Find every email address that appears more than once in `users`, with how many times it appears.

**Return:** `email`, `count`, sorted by `email`.

## Tables
- `users`: `id` int, `name` string, `email` string

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 03-duplicate-emails --engine sql --file my_answer.sql
python run.py 03-duplicate-emails --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

Group by the business key and keep groups whose size is above one. `HAVING` filters groups; `WHERE` filters rows before grouping.

</details>

<details><summary>Common mistake</summary>

Writing `WHERE COUNT(*) > 1`: aggregates are not allowed in `WHERE`.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Find Duplicate Emails](https://pyspark.in/challenges/find-duplicate-emails/)
