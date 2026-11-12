class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        incr = 1 #initilise
        decr = 1
        ans = 1

        for i in range(1, len(nums)): #chk frm 2nd element onwards
            if nums[i] > nums[i-1]:
                incr += 1
            else:
                incr = 1
            if nums[i] < nums[i-1]:
                decr += 1
            else:
                decr =1

            ans = max(ans, incr, decr)
        return ans