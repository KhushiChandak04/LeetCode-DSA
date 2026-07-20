# Write your MySQL query statement below
SELECT user_id,
    #first letter uppercase followed by all lowercase letters
    CONCAT(
        UPPER(SUBSTRING(name, 1, 1)), #(string,start position, length) SQL HAS 1 STARTING INDEXING AND NOT 0 INDEXED
        LOWER(SUBSTRING(name, 2)) #(string, start_position)
    ) AS name
FROM Users
ORDER BY user_id