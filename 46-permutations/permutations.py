class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        current = []
        used = [False] * len(nums) #initilise dp array

        def backtrack():
            if len(current) == len(nums): #found 1 permutation
                answer.append(current[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue #skip already used nos.

                current.append(nums[i]) #choose
                used[i] = True
                backtrack()

                #undo current choice
                current.pop()
                used[i] = False
            
        backtrack() #call the backtrack function here
        return answer