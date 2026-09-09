class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0 #initilise
        number = 1000 #first comma starts from 1k

        while number <= n:
            ans += n - number + 1
            number *= 1000 #move to next comma position, each time we multiply by 1k, comma added
        return ans