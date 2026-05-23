class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf') #initialise to infinity large number
        max_profit = 0 #initialse to lowest profit

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit