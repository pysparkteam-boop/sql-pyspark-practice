# 02. Filter Numeric Values Stored as Strings (SQL)

**Level:** Easy · **Topic:** Filtering / data cleaning

## Task
`transactions.amount` is text. Keep only rows whose trimmed amount is a valid number (optional leading minus, digits, optional `.digits`) and return it as `DECIMAL(12,2)`. Empty strings, `N/A`, `1,000`, `+42`, `3.` and `.5` are invalid; `007` is valid.

**Return:** `tx_id`, `customer`, `amount` (numeric), sorted by `tx_id`.

## Tables
- `transactions`: `tx_id` int, `customer` string, `amount` string

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 02-numeric-strings --engine sql --file my_answer.sql
python run.py 02-numeric-strings --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

Validate the string's shape with a regular expression *before* casting. `TRIM` first so `' 500 '` passes.

</details>

<details><summary>Common mistake</summary>

Casting first. MySQL turns `CAST('abc' AS DECIMAL)` into `0` without an error, so invalid rows survive as zeros.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

MySQL variant: `WHERE TRIM(amount) REGEXP '^-?[0-9]+(\\.[0-9]+)?$'`

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [Filter Numeric Values Stored as Strings (SQL)](https://pyspark.in/challenges/filter-numeric-values-stored-as-strings-sql/)
