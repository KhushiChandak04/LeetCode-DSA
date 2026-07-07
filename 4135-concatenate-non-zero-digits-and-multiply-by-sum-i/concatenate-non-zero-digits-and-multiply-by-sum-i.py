class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = "" #stores non 0 digits here
        digit_sum = 0 #initilise sum to 0

        for digit in str(n):
            if digit != '0':
                x += digit
                digit_sum += int(digit)
        if x == "":
            return 0
        return int(x) * digit_sum