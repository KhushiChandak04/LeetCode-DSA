# Write your MySQL query statement below
SELECT product_name, year, price
FROM Sales
INNER JOIN Product #inner join as we onli need matching rows
ON Sales.product_id = Product.product_id