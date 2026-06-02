class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        max_index = 0 #initialise maximum index as 0
        for i in range(n):
            if i > max_index: #traverse array
                return False #cannot proceed ahead
            max_index = max(max_index, i+nums[i])
        return True