class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #core idea - approach thru binary search such that mid * mid <= num
        left = 0
        right = x

        answer = 0

        while left <= right:
            mid = (left+right) // 2

            if mid*mid == x:
                return mid
            if mid*mid < x:
                answer = mid
                left = mid+1 #try bigger nos
            else:
                right = mid-1 #try out a smaller number
        return answer