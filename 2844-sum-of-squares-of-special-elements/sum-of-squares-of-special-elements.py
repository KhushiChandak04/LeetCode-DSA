class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        for i in range(1, n+1): #check every element starting frm 1 as div by 0 is n.d.
            if n % i == 0:
                ans += nums[i-1] * nums[i-1] #add square of that no.
        return ans