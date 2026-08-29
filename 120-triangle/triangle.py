class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #this is a dp problem, so we start with a copy of the bottom row
        n = len(triangle)
        dp = triangle[-1][:]

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1]) #min of left and right subtree
        return dp[0]