class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        original = n
        digitSum = 0 #initilise
        digitProduct = 1

        while n > 0:
            digit = n % 10 #to get the last digit
            digitSum += digit
            digitProduct *= digit
            n = n // 10 #remove the last digit and take the next digit to its left
        total = digitSum + digitProduct

        return original % total == 0 #check if original number is divisible by this total