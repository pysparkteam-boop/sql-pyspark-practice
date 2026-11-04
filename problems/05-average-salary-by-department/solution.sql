-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT department, ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;
