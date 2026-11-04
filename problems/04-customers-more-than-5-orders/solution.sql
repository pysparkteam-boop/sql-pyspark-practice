-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT c.customer_id, c.customer_name, COUNT(*) AS order_count
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(*) > 5
ORDER BY order_count DESC;
