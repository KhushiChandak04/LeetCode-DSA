class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m+1) for _ in range(n+1)]

        #edge case if word2 is empty delete all char of word1
        for i in range(n+1):
            dp[i][m] = n - i
        #if word1 is empty add all remaining chars
        for j in range(m+1):
            dp[n][j] = m - j

        #fill table from bottom right
        for i in range(n-1, -1, -1): #reverse traversal
            for j in range(m -1, -1, -1):
                if word1[i] == word2[j]: #if all char match
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    insert = 1 + dp[i][j+1]
                    delete = 1 + dp[i+1][j]
                    replace = 1 + dp[i+1][j+1]
                    dp[i][j] = min(insert, delete, replace)
        return dp[0][0]