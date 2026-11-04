"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    return (t["customer"].join(t["orders"], "customer_id", "left_anti")
            .select("customer_id", "customer_name", "city")
            .orderBy("customer_id"))
