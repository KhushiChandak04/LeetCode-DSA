class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #core idea -> sequential prefix is nums[i] = nums[i-1] + 1
        s = nums[0] #initilise with first number ai index 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1: #given
                s += nums[i]
            else:
                break

        while s in nums: #if sum of prefix is present in nums array
            s += 1
        return s