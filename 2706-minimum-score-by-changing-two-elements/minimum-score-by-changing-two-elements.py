class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)

    #after sorting, it is possible to change of 2 smallest, 2 largest or smallest/2nd largest
        a = nums[n-1]-nums[2]
        b = nums[n-2]-nums[1]
        c = nums[n-3]-nums[0]

        return min(a,b,c)