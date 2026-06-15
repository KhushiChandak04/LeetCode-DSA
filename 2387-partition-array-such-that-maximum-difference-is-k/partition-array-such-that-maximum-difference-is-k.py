class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        groups = 1 #initialise the no of grps as atleast 1 subsequece exists
        left = 0
        for right in range(len(nums)):
            if nums[right] - nums[left] > k:
                groups += 1
                left = right #new grps minimum becomes nums ka right ptr
        return groups