class Solution(object):
    def findMin(self, nums):
        min_val = float('inf')
        for i in range(len(nums)):
            min_val = min(min_val, nums[i])
        return min_val        