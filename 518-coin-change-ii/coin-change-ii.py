class Solution(object):

    def change(self, amount, coins):

        n = len(coins)

        #initialising dp table, where rows = coins and cols = target from 0 to amt
        dp = [[0 for j in range(amount + 1)] for i in range(n)]

        #base case, where if fully divisible select all coins of same denomination
        for target in range(amount + 1):

            if target % coins[0] == 0:
                dp[0][target] = 1

        #fill DP table
        for index in range(1, n):

            for target in range(amount + 1):

                notTaken = dp[index - 1][target] #to not take current coin, it return to prev state

                taken = 0 #to take current coin and move to next selection

                if coins[index] <= target:

                    taken = dp[index][target - coins[index]]

                #total ways
                dp[index][target] = notTaken + taken

        return dp[n - 1][amount]