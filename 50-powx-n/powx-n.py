class Solution(object):
    def myPow(self, x, n): # x raised to power n ----> x^n
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0 or x == 1:
            return 1
        if n < 0: #handle negative powers
            x = 1/x
            n = -n
        ans = 1 #initilise 
        while n > 0: #ALSO FOR HANDLING LARGE VALUES
            if n % 2 == 1: #power is not divisible by 2 -- odd power
                ans *= x
            x *= x #for even power we SQUARE THE BASE, THEN HALF THE POWER
            n //= 2
        return ans