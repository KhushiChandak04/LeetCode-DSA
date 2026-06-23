# Write your MySQL query statement below
SELECT e.employee_id, 
    e.name, 
    COUNT(r.employee_id) AS reports_count, 
    ROUND(AVG(r.age)) AS average_age
FROM Employees e #managers
JOIN Employees r #self join is used here, reporting employesess
ON e.employee_id = r.reports_to
GROUP BY e.employee_id
ORDER BY e.employee_id