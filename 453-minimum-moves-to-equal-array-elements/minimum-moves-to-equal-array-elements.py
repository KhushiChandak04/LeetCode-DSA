class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = nums[0] #find the smallest element without sortinf
        for num in nums:
            if num < smallest:
                smallest = num
        
        moves = 0 #initilise
        for num in nums:
            moves += num - smallest
        return moves