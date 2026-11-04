-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT order_date, sales,
       LAG(sales) OVER (ORDER BY order_date)         AS prev_day_sales,
       sales - LAG(sales) OVER (ORDER BY order_date) AS dod_change
FROM daily_sales
ORDER BY order_date;
