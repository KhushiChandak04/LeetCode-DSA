# Write your MySQL query statement below
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM (
    #rank salaries in each dept in desc order
    SELECT *, DENSE_RANK() OVER ( # Highest salary = Rank 1
        PARTITION BY departmentId
        ORDER BY salary DESC
    ) AS rnk
    FROM Employee 
) e
JOIN DEPARTMENT d
ON e.departmentId = d.id
WHERE rnk <= 3 #keep onli top 3 entries here