"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    w = Window.orderBy(F.desc("salary"))  # single partition: fine for small data
    return (t["employees_wf"]
            .select("emp_id", "emp_name", "salary",
                    F.rank().over(w).alias("salary_rank"),
                    F.dense_rank().over(w).alias("salary_dense_rank"))
            .orderBy(F.desc("salary"), "emp_id"))
