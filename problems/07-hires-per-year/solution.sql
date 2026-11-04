-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT EXTRACT(YEAR FROM hire_date) AS hire_year, COUNT(*) AS hire_count
FROM employees
GROUP BY EXTRACT(YEAR FROM hire_date)
ORDER BY hire_year;
