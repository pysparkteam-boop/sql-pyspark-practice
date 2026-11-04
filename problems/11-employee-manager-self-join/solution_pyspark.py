"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    e = t["employees"].alias("e")
    m = t["employees"].alias("m")
    return (e.join(m, F.col("e.manager_id") == F.col("m.employee_id"), "left")
            .select(F.col("e.employee_id"), F.col("e.first_name"), F.col("m.first_name").alias("manager_name"))
            .orderBy("employee_id"))
