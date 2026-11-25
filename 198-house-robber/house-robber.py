class Solution(object):
    def rob(self, nums):
        n = len(nums)
        dp = [0]*n #initilise a dp array

        dp[0] = nums[0] #max money frm 1st house

        if n == 1:
            return dp[0]
        dp[1] = max(nums[0],nums[1]) #choose the house with most money as the 1st one

        for i in range(2,n):
            pick = nums[i] + dp[i-2] #rob current
            not_pick = dp[i-1] #skip current
            dp[i] = max(pick,not_pick)
        return dp[n-1]