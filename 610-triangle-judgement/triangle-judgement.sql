# Write your MySQL query statement below
SELECT x, y, z,
    CASE 
        WHEN x + y > z #sum of any 2 sides greater than the 3rd
        AND x + z > y #must satisfy all 3 conditions
        AND y + z > x
        THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle