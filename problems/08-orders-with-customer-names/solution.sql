-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT o.order_id, o.order_date, c.customer_name
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
ORDER BY o.order_id;
