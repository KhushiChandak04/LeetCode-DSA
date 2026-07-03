class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = [] #stores final ans
        current = [] #stores onli the current subset we are building

        def backtrack(index):
            if index == len(nums): #traversed all nums in the list
                answer.append(current[:]) #store a copy of current subset
                return
            #choice 1: include current element
            current.append(nums[index])
            backtrack(index + 1)

            current.pop() #undo the current choice
            backtrack(index + 1) #choice 2: exclude the current choice

        backtrack(0)
        return answer