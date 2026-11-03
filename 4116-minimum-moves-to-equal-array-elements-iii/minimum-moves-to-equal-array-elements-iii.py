class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find the largest element
        largest = nums[0]
        for num in nums:
            if num > largest:
                largest = num

        # calculate moves needed to make every element equal to largest
        moves = 0
        for num in nums:
            moves += largest - num

        return moves