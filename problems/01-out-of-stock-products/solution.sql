-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT product_id, product_name
FROM products
WHERE stock_quantity = 0
ORDER BY product_id;
