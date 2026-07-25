class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = []
        while n > 0:
            digits.append(n % 10) #appends one digit at a time
            n //= 10
        digits.sort()
        return digits[-1] * digits[-2] #prod of largest and 2nd largest