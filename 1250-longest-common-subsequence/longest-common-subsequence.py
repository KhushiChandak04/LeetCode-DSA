class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m = len(text2)
        dp = [[0]* (m+1) for _ in range (n+1)] #initialise dp
        for i in range(1, n+1): #fill dp table
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]: #if char match
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:                       #if char do not match
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) #ignore current from both texts
        return dp[n][m]