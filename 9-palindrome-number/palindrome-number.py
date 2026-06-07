class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        revNum = 0 #initialise
        dummy = x #stores original num
        while x > 0:
            lastdigit = x % 10
            revNum = (revNum * 10) + lastdigit
            x //= 10
        return dummy == revNum