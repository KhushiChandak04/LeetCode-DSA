class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        #core idea is 0/1 knapsack prob... whether to take a subset or leave it, traversal is always backwards here, use dp, i zeroes and j ones
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for s in strs:
            zeroes = s.count("0")
            ones = s.count("1")

            for i in range(m, zeroes -1, -1): #go backwards so that we dnt use same string twice
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeroes][j-ones] + 1) #take current string if its beneficial

        return dp[m][n]