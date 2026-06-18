class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        freq = {} #list for storing freq
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            if freq[i] > n // 2:
                return i