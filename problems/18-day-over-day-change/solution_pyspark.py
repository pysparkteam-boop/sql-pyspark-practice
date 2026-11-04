"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    w = Window.orderBy("order_date")
    prev = F.lag("sales").over(w)
    return (t["daily_sales"]
            .select("order_date", "sales", prev.alias("prev_day_sales"), (F.col("sales") - prev).alias("dod_change"))
            .orderBy("order_date"))
