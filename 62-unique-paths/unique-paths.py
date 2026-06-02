class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[0] *n for _ in range (m)] #initialise m*n dp
        for j in range(n):
            dp[0][j] = 1 #base case for first row 1
        for i in range(m):
            dp[i][0] = 1 #base case for first column 1
        for i in range(1,m): #for filling all value
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1] #the corner most element gives the total count here