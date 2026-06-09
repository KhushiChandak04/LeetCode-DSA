class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxVal = max(nums) #largest value in the array
        minVal = min(nums) #smallest value in the array
        bestVal = maxVal - minVal
        return bestVal * k #same subarray can be chosen k times