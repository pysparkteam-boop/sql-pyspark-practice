"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    return (t["products"]
            .filter(F.col("stock_quantity") == 0)
            .select("product_id", "product_name")
            .orderBy("product_id"))
