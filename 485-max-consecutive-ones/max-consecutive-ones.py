class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        count = 0
        for num in nums:
            if num == 1: #count consecutive 1's
                count += 1
                max_count = max(count, max_count)
            else: #break in the streak
                count = 0
        return max_count