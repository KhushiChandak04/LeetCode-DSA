class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        #if num is negative, convert it into 32 bit repr
        if num < 0:
            num = num + 2**32
        
        digits = '0123456789abcdef' #hexa symbols

        if num == 0:
            return '0'

        ans = "" #blank string to store ans
        
        while num > 0:
            remainder = num % 16
            ans = digits[remainder] + ans
            num //= 16
        return ans