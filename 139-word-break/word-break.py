class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        word_set = set(wordDict)
        dp = [False] * (n+1) #initialise to false
        dp[0] = True #base case if nothing is selected

        for i in range (1, n+1): #we start from 1 as 0 base case is laready defined
            for j in range (i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
        return dp[n]