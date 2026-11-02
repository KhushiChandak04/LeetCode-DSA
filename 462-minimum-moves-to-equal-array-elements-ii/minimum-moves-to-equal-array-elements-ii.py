class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        # find the middle element (median)
        mid = len(nums) // 2
        median = nums[mid]

        # calculate total moves required
        moves = 0
        for num in nums:
            moves += abs(num - median)

        return moves