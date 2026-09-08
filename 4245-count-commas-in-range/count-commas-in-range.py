class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1000: #numbers less than 1000 do not have commas
            return 0
        return n - 999 #1000 onwards 1 comma