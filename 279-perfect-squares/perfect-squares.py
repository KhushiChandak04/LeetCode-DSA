class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        #dp array problem
        dp = [float('inf')]*(n+1) #initilise
        dp[0] = 0 #base case, 0 needs 0 squares

        for i in range(1,n+1):
            j = 1 #chk every possible perfect square, we use j ptr here
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-j*j] +1) #rem amt after subtracting the perfeect square
                j += 1
        return dp[n]