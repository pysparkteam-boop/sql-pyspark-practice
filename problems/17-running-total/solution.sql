-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT order_date, sales,
       SUM(sales) OVER (ORDER BY order_date
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM daily_sales
ORDER BY order_date;
