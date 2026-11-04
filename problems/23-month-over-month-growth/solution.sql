-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT month_start, sales,
       LAG(sales) OVER (ORDER BY month_start) AS prev_month_sales,
       ROUND((sales - LAG(sales) OVER (ORDER BY month_start)) * 100.0
             / LAG(sales) OVER (ORDER BY month_start), 2) AS mom_growth_pct
FROM monthly_sales
ORDER BY month_start;
