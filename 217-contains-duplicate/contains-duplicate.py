class Solution(object):
    def containsDuplicate(self, nums):
        unique = set(nums)
        return len(unique) < len(nums)