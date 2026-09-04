class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            left_max = max(nums[0:i+1])
            right_min = min(nums[i:]) #right side of i ka min value

            if left_max - right_min <= k: #check stability score
                return i
        return -1