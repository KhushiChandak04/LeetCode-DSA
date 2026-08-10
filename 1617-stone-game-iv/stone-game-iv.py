class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [False] * (n+1) #initilise dp array
        for i in range(1,n+1): #as no negative vals
            j = 1 #try every possible square number
            while j * j <= i: #less than or equal to square val, stone can be removed
                if dp[i-j*j] == False: #after removing the j*j leaves opponent
                    dp[i] = True
                    break
                j += 1
        return dp[n]