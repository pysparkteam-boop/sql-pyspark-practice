-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT emp_id, emp_name, salary,
       RANK()       OVER (ORDER BY salary DESC) AS salary_rank,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_dense_rank
FROM employees_wf
ORDER BY salary DESC, emp_id;
