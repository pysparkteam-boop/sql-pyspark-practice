"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    return (t["orders"].join(t["customers"], "customer_id")
            .select("order_id", "order_date", "customer_name")
            .orderBy("order_id"))
