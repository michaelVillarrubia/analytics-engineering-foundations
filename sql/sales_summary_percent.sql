SELECT
    category,
    SUM(amount) AS total_sales,
	ROUND(
	SUM(amount) / (SELECT SUM(amount) FROm sale) * 100,
	2
	) AS percent_of_total
FROM sale
GROUP BY category
ORDER BY total_sales DESC;