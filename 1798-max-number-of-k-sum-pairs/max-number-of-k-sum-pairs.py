class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #we use 2 ptr approach to reduct time complexity
        nums.sort()
        left = 0
        right = len(nums) - 1 #initialise ptrs
        count = 0
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == k:
                count += 1
                left += 1
                right -= 1
            elif curr_sum < k:
                left += 1
            else:
                right -= 1
        return count