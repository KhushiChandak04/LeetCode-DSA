class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        smallest = float('inf') #start with the largest val

        for i in range(len(nums)):
            total = 0 #initilise

            for j in range(i,len(nums)):
                total += nums[j]
                length = j-i+1 #len of curr subarray

                if length >= l and length <= r:
                    if total >0 and total < smallest: #given condition
                        smallest = total

        if smallest == float('inf'):
            return -1
            
        return smallest