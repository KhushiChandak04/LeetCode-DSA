class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort( reverse = True)
        #ways to get max product -> 3 largest OR 2 -ve and 1 largest +ve
        return max(
            nums[0] * nums[1] * nums[2], #top 3 largest in desc order
            nums[-1] * nums[-2] * nums[0] #2 -ve and 1 largest +ve
        )