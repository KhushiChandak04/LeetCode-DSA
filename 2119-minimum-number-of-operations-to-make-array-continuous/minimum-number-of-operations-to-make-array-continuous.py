class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = sorted(set(nums)) #sorted array, using sets helps us to remove duplicates

        left = 0
        largest = 0

        for right in range(len(nums)):

            while nums[right] - nums[left] >= n: #remove elements outside of req range
                left += 1
            largest = max(largest, right-left+1)
        
        return n-largest #replace outside largest grp