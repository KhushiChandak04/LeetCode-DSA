class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #we do not use brute force here as it will take o(n log n) complexity
        n = len(nums)
        freq = [0] * (n+1) #frequency array
        for i in nums:
            if freq[i] == 0: #first occurance
                freq[i] += 1
            else: #already seen
                return i