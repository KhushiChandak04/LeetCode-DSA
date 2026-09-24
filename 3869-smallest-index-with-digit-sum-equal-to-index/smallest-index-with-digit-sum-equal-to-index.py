class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            num = nums[i] #take current number
            total = 0 #take total till curr val

            while num > 0: #calculate sum of digits
                total += num % 10
                num = num // 10
            if total == i:
                return i
                
        return -1 #if no index found