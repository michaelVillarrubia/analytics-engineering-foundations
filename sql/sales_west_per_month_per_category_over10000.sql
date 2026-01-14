SELECT DATE_TRUNC('month', sale_date), category, 
SUM(amount) 
FROM sales 
WHERE region = 'West' 
GROUP BY DATE_TRUNC('month', sale_date), category 