# Write your MySQL query statement below
-- Find total amount spent on each day
WITH daily AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
)

SELECT
    visited_on,

    -- Sum of current day + previous 6 days
    SUM(amount) OVER (
        ORDER BY visited_on
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS amount,

    -- Average of the 7-day window
    ROUND(
        AVG(amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ), 2
    ) AS average_amount

FROM daily

-- Ignore first 6 days (need a complete 7-day window)
LIMIT 1000000 OFFSET 6;