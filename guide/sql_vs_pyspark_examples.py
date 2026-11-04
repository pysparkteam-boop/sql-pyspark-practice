"""Every example in the SQL vs PySpark guide, executed on ONE shared dataset.

Each example is a (SQL, PySpark) pair. The SQL runs on DuckDB, the PySpark on local Spark 3.5.
The script asserts both return the same rows, and writes guide/outputs.md with each result table
so the guide shows real, reproducible output. Run:  python guide/sql_vs_pyspark_examples.py
"""
import datetime as dt
import os
from decimal import Decimal

import duckdb
from pyspark.sql import SparkSession, Window
from pyspark.sql import functions as F

HERE = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ the shared dataset (synthetic)
CUSTOMERS = [  # customer_id, name, city, signup_date
    (1, "Asha", "Pune", dt.date(2024, 1, 5)),
    (2, "Ravi", "Delhi", dt.date(2024, 1, 20)),
    (3, "Meera", None, dt.date(2024, 2, 2)),
    (4, "Kabir", "Pune", dt.date(2024, 3, 15)),
    (5, "Zoya", "Mumbai", dt.date(2024, 3, 28)),
]
ORDERS = [  # order_id, customer_id, order_date, amount, status
    (101, 1, dt.date(2024, 2, 1), Decimal("250.00"), "delivered"),
    (102, 1, dt.date(2024, 2, 15), Decimal("400.00"), "delivered"),
    (103, 2, dt.date(2024, 2, 3), Decimal("150.00"), "cancelled"),
    (104, 2, dt.date(2024, 3, 9), Decimal("400.00"), "delivered"),
    (105, 3, dt.date(2024, 3, 10), None, "pending"),
    (106, 4, dt.date(2024, 3, 22), Decimal("90.00"), "delivered"),
    (107, 1, dt.date(2024, 3, 30), Decimal("120.00"), "delivered"),
    (108, 9, dt.date(2024, 3, 31), Decimal("75.00"), "delivered"),   # customer 9 does not exist
    (107, 1, dt.date(2024, 3, 30), Decimal("120.00"), "delivered"),  # exact duplicate row (ingestion retry)
]
CUST_DDL = "customer_id INT, name STRING, city STRING, signup_date DATE"
ORD_DDL = "order_id INT, customer_id INT, order_date DATE, amount DECIMAL(10,2), status STRING"

con = duckdb.connect()
con.execute("CREATE TABLE customers (customer_id INTEGER, name VARCHAR, city VARCHAR, signup_date DATE)")
con.execute("CREATE TABLE orders (order_id INTEGER, customer_id INTEGER, order_date DATE, amount DECIMAL(10,2), status VARCHAR)")
con.executemany("INSERT INTO customers VALUES (?, ?, ?, ?)", CUSTOMERS)
con.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", ORDERS)

spark = (SparkSession.builder.master("local[1]").appName("sql-vs-pyspark-guide")
         .config("spark.sql.shuffle.partitions", "1").config("spark.ui.enabled", "false")
         .config("spark.sql.session.timeZone", "UTC").getOrCreate())
spark.sparkContext.setLogLevel("ERROR")
customers = spark.createDataFrame(CUSTOMERS, CUST_DDL)
orders = spark.createDataFrame(ORDERS, ORD_DDL)
customers.createOrReplaceTempView("customers")
orders.createOrReplaceTempView("orders")

EXAMPLES = []


def ex(key, title, sql, pyspark, ordered=True, spark_sql_too=True):
    EXAMPLES.append(dict(key=key, title=title, sql=sql.strip(), pyspark=pyspark, ordered=ordered, spark_sql_too=spark_sql_too))


# ------------------------------------------------------------------ 1. SELECT and filtering
ex("select-filter", "Delivered orders over 100",
   """SELECT order_id, customer_id, amount
FROM orders
WHERE status = 'delivered' AND amount > 100
ORDER BY order_id""",
   lambda: (orders.filter((F.col("status") == "delivered") & (F.col("amount") > 100))
            .select("order_id", "customer_id", "amount").orderBy("order_id")))

ex("case-when", "CASE WHEN vs when().otherwise()",
   """SELECT order_id, amount,
       CASE WHEN amount >= 300 THEN 'large'
            WHEN amount >= 100 THEN 'medium'
            ELSE 'small' END AS size
FROM orders
WHERE amount IS NOT NULL
ORDER BY order_id""",
   lambda: (orders.filter(F.col("amount").isNotNull())
            .select("order_id", "amount",
                    F.when(F.col("amount") >= 300, "large")
                     .when(F.col("amount") >= 100, "medium")
                     .otherwise("small").alias("size"))
            .orderBy("order_id")))

# ------------------------------------------------------------------ 2. GROUP BY and aggregation
ex("group-by", "Orders and revenue per customer (delivered only), keep customers above 300",
   """SELECT customer_id, COUNT(*) AS orders, SUM(amount) AS revenue
FROM orders
WHERE status = 'delivered'
GROUP BY customer_id
HAVING SUM(amount) > 300
ORDER BY revenue DESC""",
   lambda: (orders.filter(F.col("status") == "delivered")
            .groupBy("customer_id")
            .agg(F.count("*").alias("orders"), F.sum("amount").alias("revenue"))
            .filter(F.col("revenue") > 300)
            .orderBy(F.desc("revenue"))))

# ------------------------------------------------------------------ 3. Joins
ex("inner-join", "INNER JOIN: orders with customer names",
   """SELECT o.order_id, c.name, o.amount
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
WHERE o.order_id < 105
ORDER BY o.order_id""",
   lambda: (orders.join(customers, "customer_id")
            .filter(F.col("order_id") < 105)
            .select("order_id", "name", "amount").orderBy("order_id")))

ex("left-join", "LEFT JOIN: every customer with their order count (zero included)",
   """SELECT c.customer_id, c.name, COUNT(o.order_id) AS orders
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY c.customer_id""",
   lambda: (customers.join(orders, "customer_id", "left")
            .groupBy("customer_id", "name")
            .agg(F.count("order_id").alias("orders"))
            .orderBy("customer_id")))

ex("anti-join", "Anti join: customers with no orders",
   """SELECT c.customer_id, c.name
FROM customers c
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id)
ORDER BY c.customer_id""",
   lambda: customers.join(orders, "customer_id", "left_anti").select("customer_id", "name").orderBy("customer_id"))

ex("orphans", "Anti join the other way: orders whose customer does not exist",
   """SELECT o.order_id, o.customer_id
FROM orders o
LEFT JOIN customers c ON c.customer_id = o.customer_id
WHERE c.customer_id IS NULL""",
   lambda: orders.join(customers, "customer_id", "left_anti").select("order_id", "customer_id"),
   ordered=False)

# ------------------------------------------------------------------ 4. Window functions / ranking
ex("ranking", "ROW_NUMBER, RANK and DENSE_RANK on the same rows",
   """SELECT order_id, amount,
       ROW_NUMBER() OVER (ORDER BY amount DESC, order_id) AS row_number,
       RANK()       OVER (ORDER BY amount DESC)           AS rank,
       DENSE_RANK() OVER (ORDER BY amount DESC)           AS dense_rank
FROM (SELECT DISTINCT * FROM orders) d
WHERE amount IS NOT NULL
ORDER BY row_number""",
   lambda: (orders.distinct().filter(F.col("amount").isNotNull())
            .select("order_id", "amount",
                    F.row_number().over(Window.orderBy(F.desc("amount"), "order_id")).alias("row_number"),
                    F.rank().over(Window.orderBy(F.desc("amount"))).alias("rank"),
                    F.dense_rank().over(Window.orderBy(F.desc("amount"))).alias("dense_rank"))
            .orderBy("row_number")))

ex("top-n-per-group", "Latest order per customer (top 1 per group)",
   """SELECT customer_id, order_id, order_date
FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id
                                 ORDER BY order_date DESC, order_id DESC) AS rn
    FROM orders
) x
WHERE rn = 1
ORDER BY customer_id""",
   lambda: (orders.withColumn("rn", F.row_number().over(
                Window.partitionBy("customer_id").orderBy(F.desc("order_date"), F.desc("order_id"))))
            .filter("rn = 1").select("customer_id", "order_id", "order_date").orderBy("customer_id")))

ex("running-total", "Running total of delivered revenue by date",
   """SELECT order_date, SUM(amount) AS day_revenue,
       SUM(SUM(amount)) OVER (ORDER BY order_date
                              ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_revenue
FROM (SELECT DISTINCT * FROM orders WHERE status = 'delivered') d
GROUP BY order_date
ORDER BY order_date""",
   lambda: (orders.filter(F.col("status") == "delivered").distinct()
            .groupBy("order_date").agg(F.sum("amount").alias("day_revenue"))
            .withColumn("running_revenue", F.sum("day_revenue").over(
                Window.orderBy("order_date").rowsBetween(Window.unboundedPreceding, Window.currentRow)))
            .orderBy("order_date")))

ex("lag", "Previous order amount per customer (LAG)",
   """SELECT customer_id, order_id, amount,
       LAG(amount) OVER (PARTITION BY customer_id ORDER BY order_date, order_id) AS prev_amount
FROM (SELECT DISTINCT * FROM orders) d
WHERE customer_id IN (1, 2)
ORDER BY customer_id, order_id""",
   lambda: (orders.distinct().filter(F.col("customer_id").isin(1, 2))
            .withColumn("prev_amount", F.lag("amount").over(
                Window.partitionBy("customer_id").orderBy("order_date", "order_id")))
            .select("customer_id", "order_id", "amount", "prev_amount").orderBy("customer_id", "order_id")))

# ------------------------------------------------------------------ 5. CTEs
ex("cte", "CTE vs a DataFrame variable: customers above the average customer revenue",
   """WITH revenue AS (
    SELECT customer_id, SUM(amount) AS revenue
    FROM (SELECT DISTINCT * FROM orders) d
    WHERE status = 'delivered'
    GROUP BY customer_id
)
SELECT customer_id, revenue
FROM revenue
WHERE revenue > (SELECT AVG(revenue) FROM revenue)
ORDER BY customer_id""",
   lambda: (lambda revenue: revenue.filter(F.col("revenue") > revenue.agg(F.avg("revenue")).first()[0])
            .orderBy("customer_id"))(
       orders.distinct().filter(F.col("status") == "delivered").groupBy("customer_id").agg(F.sum("amount").alias("revenue"))))

# ------------------------------------------------------------------ 6. NULL handling
ex("count-null", "COUNT(*) vs COUNT(column) vs SUM with NULLs",
   """SELECT COUNT(*) AS all_rows, COUNT(amount) AS with_amount, SUM(amount) AS total
FROM orders""",
   lambda: orders.agg(F.count("*").alias("all_rows"), F.count("amount").alias("with_amount"), F.sum("amount").alias("total")))

ex("coalesce", "COALESCE / fillna for display",
   """SELECT customer_id, name, COALESCE(city, 'unknown') AS city
FROM customers
ORDER BY customer_id""",
   lambda: customers.select("customer_id", "name", F.coalesce("city", F.lit("unknown")).alias("city")).orderBy("customer_id"))

ex("null-equality", "NULL never equals NULL: = vs IS NOT DISTINCT FROM vs eqNullSafe",
   """SELECT customer_id, city,
       city = city                    AS plain_equals,
       city IS NOT DISTINCT FROM city AS null_safe_equals
FROM customers
ORDER BY customer_id""",
   lambda: (customers.select("customer_id", "city",
                             (F.col("city") == F.col("city")).alias("plain_equals"),
                             F.col("city").eqNullSafe(F.col("city")).alias("null_safe_equals"))
            .orderBy("customer_id")),
   spark_sql_too=False)  # Spark SQL spells it <=> ; verified in verify_spark_sql_spellings.py

# ------------------------------------------------------------------ 7. Duplicates
ex("distinct", "Remove exact duplicate rows: DISTINCT vs distinct()",
   """SELECT COUNT(*) AS rows_after
FROM (SELECT DISTINCT * FROM orders) d""",
   lambda: orders.distinct().agg(F.count("*").alias("rows_after")))

ex("dedupe-key", "Keep one row per key, deterministically",
   """SELECT order_id, customer_id, amount
FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY order_date DESC) AS rn
    FROM orders
) x
WHERE rn = 1 AND order_id = 107""",
   lambda: (orders.withColumn("rn", F.row_number().over(Window.partitionBy("order_id").orderBy(F.desc("order_date"))))
            .filter("rn = 1 AND order_id = 107").select("order_id", "customer_id", "amount")),
   ordered=False)

# ------------------------------------------------------------------ 8. Median
ex("median", "Median order amount per status",
   """SELECT status, MEDIAN(amount) AS median_amount
FROM (SELECT DISTINCT * FROM orders) d
WHERE amount IS NOT NULL
GROUP BY status
ORDER BY status""",
   lambda: (orders.distinct().filter(F.col("amount").isNotNull())
            .groupBy("status").agg(F.median("amount").alias("median_amount")).orderBy("status")),
   spark_sql_too=True)

ex("median-portable", "Median without a MEDIAN function (works on MySQL 8)",
   """SELECT AVG(amount) AS median_amount
FROM (
    SELECT amount,
           ROW_NUMBER() OVER (ORDER BY amount) AS rn,
           COUNT(*)     OVER ()                AS n
    FROM (SELECT DISTINCT * FROM orders) d
    WHERE amount IS NOT NULL AND status = 'delivered'
) x
WHERE rn IN ((n + 1) DIV 2, (n + 2) DIV 2)""".replace(" DIV ", " // "),
   lambda: (orders.distinct().filter(F.col("amount").isNotNull() & (F.col("status") == "delivered"))
            .agg(F.percentile("amount", 0.5).alias("median_amount"))),
   spark_sql_too=False)

# ------------------------------------------------------------------ 9. Dates
ex("dates", "Month, days since signup and month arithmetic",
   """SELECT o.order_id,
       CAST(date_trunc('month', o.order_date) AS DATE)  AS order_month,
       date_diff('day', c.signup_date, o.order_date)    AS days_since_signup,
       CAST(o.order_date + INTERVAL 1 MONTH AS DATE)    AS follow_up_date
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
WHERE o.order_id IN (101, 104, 106)
ORDER BY o.order_id""",
   lambda: (orders.join(customers, "customer_id").filter(F.col("order_id").isin(101, 104, 106))
            .select("order_id", F.trunc("order_date", "month").alias("order_month"),
                    F.datediff("order_date", "signup_date").alias("days_since_signup"),
                    F.add_months("order_date", 1).alias("follow_up_date"))
            .orderBy("order_id")),
   spark_sql_too=False)  # DuckDB date syntax differs from Spark SQL; the guide shows the Spark SQL spelling

ex("monthly", "Revenue per month",
   """SELECT CAST(date_trunc('month', order_date) AS DATE) AS month, SUM(amount) AS revenue
FROM (SELECT DISTINCT * FROM orders WHERE status = 'delivered') d
GROUP BY 1
ORDER BY 1""",
   lambda: (orders.filter(F.col("status") == "delivered").distinct()
            .groupBy(F.trunc("order_date", "month").alias("month")).agg(F.sum("amount").alias("revenue"))
            .orderBy("month")),
   spark_sql_too=False)


# ------------------------------------------------------------------ run + compare
def norm(v):
    if isinstance(v, (Decimal, float)) and v is not None:
        return format(Decimal(str(v)).quantize(Decimal("0.01")), "f")
    if isinstance(v, (dt.date, dt.datetime)):
        return v.isoformat()
    return v


def table_md(cols, rows):
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        out.append("| " + " | ".join("NULL" if v is None else str(norm(v)) for v in r) + " |")
    return "\n".join(out)


def main():
    md, failures = ["# Generated outputs (do not edit; produced by guide_examples.py)\n"], 0
    for e in EXAMPLES:
        res = con.execute(e["sql"])
        cols = [d[0] for d in res.description]
        sql_rows = [tuple(norm(v) for v in r) for r in res.fetchall()]
        df = e["pyspark"]()
        py_rows = [tuple(norm(v) for v in r) for r in df.collect()]
        same = sql_rows == py_rows if e["ordered"] else sorted(map(repr, sql_rows)) == sorted(map(repr, py_rows))
        spark_sql_ok = None
        if e["spark_sql_too"]:
            sp = [tuple(norm(v) for v in r) for r in spark.sql(e["sql"]).collect()]
            spark_sql_ok = sp == sql_rows if e["ordered"] else sorted(map(repr, sp)) == sorted(map(repr, sql_rows))
        ok = same and spark_sql_ok is not False
        failures += 0 if ok else 1
        print("%s  %-18s duckdb=pyspark:%s  spark.sql:%s  rows=%d" % ("PASS" if ok else "FAIL", e["key"], same,
              "n/a" if spark_sql_ok is None else spark_sql_ok, len(sql_rows)))
        if not ok:
            print("   duckdb :", sql_rows, "\n   pyspark:", py_rows)
        md.append("## %s\n\n%s\n" % (e["key"], table_md(cols, sql_rows)))
    with open(os.path.join(HERE, "outputs.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print("\n%d examples, %d failures" % (len(EXAMPLES), failures))
    return failures


if __name__ == "__main__":
    raise SystemExit(main())
