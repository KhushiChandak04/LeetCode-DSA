class Solution(object):
    def climbStairs(self, n):
        dp = [-1] * (n+1) #this is how we initialise a dp, standard format
        dp[0] = 1
        dp[1] = 1 #for base cases

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2] #fibonacchi logic
        return(dp[n])