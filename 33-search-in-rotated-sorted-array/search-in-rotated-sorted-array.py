class Solution(object):
    def search(self, nums, target):
        n = len(nums)

        for i in range(n):
            if nums[i] == target:
                return i
        return -1