class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #initilise dp[i] = min coins needed to fulfil amount i
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0 #base condn, 0 coins is 0 amt

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i: #can this coin contribute to i?
                    dp[i] = min(dp[i], dp[i - coin] + 1) #either take this coin or take it once

        if dp[amount] == float("inf"):
            return -1
        return dp[amount]