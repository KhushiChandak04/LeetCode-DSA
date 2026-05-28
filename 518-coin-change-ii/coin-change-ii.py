class Solution(object):

    def change(self, amount, coins):

        #initialising dp array from 0 to target amount
        dp = [0] * (amount + 1)

        #base case, there is 1 way to make target 0 i.e choose nothing
        dp[0] = 1

        #traverse every coin one by one
        for coin in coins:

            #start from current coin till target amount
            for target in range(coin, amount + 1):

                #adding ways of forming remaining target after taking current coin
                dp[target] += dp[target - coin]

        #return total no of ways for final target amount
        return dp[amount]