class Solution(object):
    def robLinear(self, nums):
        n = len(nums)
        if n == 0: #if 0 houses
            return 0
        if n == 1: #if only 1 house
            return nums[0]
        dp = [0] * n #initialise dp array
        dp[0] = nums[0] #base case
        for i in range(1,n):
            pick = nums[i]
            if i > 1:
                pick = pick + dp[i-2] #dont rob adjecent leave one in between
            notPick = dp[i-1]
            dp[i] = max(pick, notPick)
        return dp[n-1]
    
    #for circular case, we create an new function
    def rob(self, nums):
        n = len(nums)
        if n ==1:
            return nums[0]
        case1 = self.robLinear(nums[1:]) #excludes 1st house
        case2 = self.robLinear(nums[:-1]) #excludes last house
        return max(case1, case2)