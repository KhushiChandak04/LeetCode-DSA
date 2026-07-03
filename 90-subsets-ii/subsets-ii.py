class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() #brings all duplicates together
        answer = []
        current = []

        def backtrack(start):
            answer.append(current[:]) #store every subset
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums [i - 1]: #duplicate skips
                    continue
                current.append(nums[i])
                backtrack(i+1)
                current.pop() #backtrack
        backtrack(0)
        return answer