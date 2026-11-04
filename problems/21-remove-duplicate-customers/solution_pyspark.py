"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    w = Window.partitionBy("customer_name", "email", "phone").orderBy("customer_id")
    return (t["customers"]
            .withColumn("rn", F.row_number().over(w))
            .filter("rn = 1")
            .drop("rn")
            .orderBy("customer_id"))
