class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #pivot where sum nums on left = sum nums right
        total = sum(nums)
        left = 0 #sum of left side
        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
            left += nums[i] #add sum of left
        return -1