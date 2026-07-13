class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #algo must be in o(n) complexity
        s = set(nums)
        answer = 1
        while answer in s: #if the smallest +ve val is in set then increase by 1
            answer += 1
        return answer