class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = 0
        for customer in accounts:
            wealth = 0
            for money in customer:
                wealth += money
            richest = max(richest, wealth)
        return richest