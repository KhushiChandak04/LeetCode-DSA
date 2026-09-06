class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        #this is also a knapsack kinda problem that can be solved by dp array

        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        
        for i in range(len(s) + 1):
            dp[i][0] = 1 #empty t has exactly 1 way to choose from so this is the base case

        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                #if the characters are same then
                if s[i-1] == t[j-1]: #every character chk
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j] #if the characters match, either take this character or don't take it
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(s)][len(t)]