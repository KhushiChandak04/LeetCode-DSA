class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#best way is to sort and then pair neighbours for maximised sum for minimised pairings
        nums.sort()
        total = 0
        for i in range(0, len(nums) - 1, 2): #start, end, step size format
            total += nums[i]
        return total