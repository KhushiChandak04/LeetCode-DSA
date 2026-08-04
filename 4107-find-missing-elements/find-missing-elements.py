class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        minimum = min(nums)
        maximum = max(nums)
        seen = set(nums)
        result = []

        for num in range(minimum, maximum):
            if num not in seen:
                result.append(num)
        return result