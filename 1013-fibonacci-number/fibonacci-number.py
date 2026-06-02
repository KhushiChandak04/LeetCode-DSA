class Solution(object):
    def fib(self, n):
        if n<=1:
            return n
        dp = [0] * (n+1) #initialise a dp array
        dp[0] = 0 #base cases
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            i += 1
        return dp[n]