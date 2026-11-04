"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    w = Window.orderBy("month_start")
    prev = F.lag("sales").over(w)
    return (t["monthly_sales"]
            .select("month_start", "sales", prev.alias("prev_month_sales"),
                    F.round((F.col("sales") - prev) * 100.0 / prev, 2).alias("mom_growth_pct"))
            .orderBy("month_start"))
