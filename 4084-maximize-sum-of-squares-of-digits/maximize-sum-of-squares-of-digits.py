class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum > num*9: #if number is too big, nothing valid is poss
            return ""
        ans = ""

        for i in range(num): #buuild the number digit by digit
            if sum >= 9: #if sum is atleast 9, then put 9
                ans += '9'
                sum -= 9
            elif sum > 0:
                ans += str(sum)
                sum = 0
            else:
                ans += '0' #fill remainin placees by 0
        return ans