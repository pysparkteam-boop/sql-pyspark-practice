# 16. RANK vs DENSE_RANK: See the Difference Side by Side

**Level:** Easy · **Topic:** Window functions (RANK, DENSE_RANK)

## Task
Rank all employees by salary (highest first) twice: once with `RANK()` and once with `DENSE_RANK()`.

**Return:** `emp_id`, `emp_name`, `salary`, `salary_rank`, `salary_dense_rank`.

## Tables
- `employees_wf`: `emp_id` int, `emp_name` string, `department` string, `salary` int

Data: [`data/`](data/) (CSV). Expected output for this data: [`expected.csv`](expected.csv).

## Try it
```bash
python run.py 16-rank-vs-dense-rank --engine sql --file my_answer.sql
python run.py 16-rank-vs-dense-rank --engine pyspark --file my_answer.py   # define solve(t)
```

<details><summary>Approach</summary>

Both give ties the same number. `RANK` then skips (1, 2, 3, 3, 5); `DENSE_RANK` does not (1, 2, 3, 3, 4).

</details>

<details><summary>Common mistake</summary>

Using `ROW_NUMBER` when ties must share a rank.

</details>

<details><summary>Reference solutions</summary>

[`solution.sql`](solution.sql) · [`solution_pyspark.py`](solution_pyspark.py)

</details>

## Practise it online
Run it in the browser and check your answer against more test cases on PySpark.in: [RANK vs DENSE_RANK: See the Difference Side by Side](https://pyspark.in/challenges/rank-vs-dense-rank-see-the-difference-side-by-side/)
