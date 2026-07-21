# Write your MySQL query statement below
SELECT *
FROM Users
WHERE REGEXP_LIKE( #use regex
    mail,
    '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$',
    'c' #case sensitive
);