class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        if s[0] == '0': #invalid as if first char is 0, then cant decode
            return 0
        dp = [0] * (n+1) #initialise dp
        dp[0] = 1 #base cases
        dp[1] = 1
        for i in range(2, n+1):
            if s[i-1] != '0': #single digit
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26: #two digits
                dp[i] += dp[i-2]
        return dp[n]