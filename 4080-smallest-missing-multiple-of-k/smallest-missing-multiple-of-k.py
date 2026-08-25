class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = set(nums)
        multiple = k

        while multiple in s:
            multiple += k
        return multiple