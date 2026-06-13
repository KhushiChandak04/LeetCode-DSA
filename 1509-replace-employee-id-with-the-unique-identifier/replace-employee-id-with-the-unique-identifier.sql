# Write your MySQL query statement below
SELECT unique_id, name
FROM Employees
LEFT JOIN EmployeeUNI #simple left join as we are keeping all rows from left table
ON Employees.id = EmployeeUNI.id #where ids match for both table