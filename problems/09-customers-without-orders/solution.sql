-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT c.customer_id, c.customer_name, c.city
FROM customer c
LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL
ORDER BY c.customer_id;
