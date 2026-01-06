SELECT
    category,
    SUM(amount) AS total_sales
FROM sale
GROUP BY category
ORDER BY total_sales DESC;
