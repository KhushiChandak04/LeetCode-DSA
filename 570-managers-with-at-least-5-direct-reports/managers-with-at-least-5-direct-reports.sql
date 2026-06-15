# Write your MySQL query statement below
SELECT e.name
FROM Employee e
JOIN Employee emp
ON e.id = emp.managerId
GROUP BY e.id, e.name
HAVING COUNT(emp.id) >= 5 #we are filtering groups instad of rows so we use having here