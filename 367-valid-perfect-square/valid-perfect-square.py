class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 1 #binary search
        right = num

        #search for a square root
        while left <= right:
            mid = (left+right) // 2
            square = mid * mid

            if square == num: #check if mid squared is equal to num
                return True
            elif square < num:
                left = mid +1
            else:
                right = mid -1

        return False #otherwise