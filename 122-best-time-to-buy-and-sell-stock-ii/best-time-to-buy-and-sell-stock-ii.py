class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #core idea - maximise the diff, and multiple trans. allowed -> greedy method
        profit = 0 #initilise

        for i in range(1, len(prices)): #restrict to 1 as min 1 stock to hold
        #if today higher than yesterday -> take it
        #take profit
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit