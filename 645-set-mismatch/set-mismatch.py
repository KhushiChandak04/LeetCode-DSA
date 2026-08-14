class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = {} #initlise dictionary

        for num in nums:
            count[num] = count.get(num, 0) + 1 #count freq of each number

        duplicate = 0
        missing = 0 #init
        for i in range(len(nums) + 1):
            if i not in count:
                missing = i
            elif count[i] == 2:
                duplicate = i

        return [duplicate, missing]