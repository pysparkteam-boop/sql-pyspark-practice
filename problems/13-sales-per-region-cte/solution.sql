-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
WITH region_totals AS (
    SELECT region, SUM(amount) AS total_sales
    FROM sales
    GROUP BY region
)
SELECT region, total_sales
FROM region_totals
ORDER BY total_sales DESC;
