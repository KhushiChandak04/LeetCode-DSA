class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        odd_sum = n * n
        even_sum = n * (n + 1)
        while even_sum != 0:
            odd_sum, even_sum = even_sum, odd_sum % even_sum #keep on swapping vals
        return odd_sum