# Write your MySQL query statement below
SELECT p.product_id,
    ROUND(IFNULL(SUM(p.price * u.units) / SUM(u.units), 0), 2) AS average_price #price * units sold / total units
FROM Prices p
LEFT JOIN UnitsSold u
ON p.product_id = u.product_id
AND u.purchase_date BETWEEN p.start_date AND p.end_date #as we are having variation of prices in regards to dates also
GROUP BY p.product_id