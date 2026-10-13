class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        squares = [] #initilise array

        for num in nums:
            squares.append(num*num)

        squares.sort() #sort squares in asc order
        ans = 0
        n = len(squares)

        for i in range(n):
            #subtract the smaller half and add larger half

            if i < n // 2:
                ans -= squares[i]
            else:
                ans += squares[i]
        return ans