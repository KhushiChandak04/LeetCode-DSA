class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #use hashset for optimal soln
        num_set = set(nums)
        longest = 0 #initilise

        for num in num_set:

            if num - 1 not in num_set: #start only if it is the beginning of numset
                length = 1
                current = num

                while current + 1 in num_set: #until the consecutive nos in set
                    current += 1
                    length += 1
                longest = max(longest, length)

        return longest