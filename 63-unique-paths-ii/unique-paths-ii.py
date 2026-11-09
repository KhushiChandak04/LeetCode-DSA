class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid) #rows
        n = len(obstacleGrid[0]) #cols

        dp = [[0]*n for i in range(m)] #we use dynamic progr. to reject or select a path possibility here

        if obstacleGrid[0][0] == 1: #if starting cell is blocked then there is no path
            return 0 #no path

        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0 #skip obstacle cell here
                else:
                    if i > 0: #add paths from top cell here
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1] #add paths from left cell here
                        
        return dp[m-1][n-1]