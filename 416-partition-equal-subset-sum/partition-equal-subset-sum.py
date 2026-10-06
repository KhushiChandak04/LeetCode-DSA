class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums) #find total sum

        if total % 2 != 0: #if total is odd we cannt form the partititon
            return False
        target = total // 2 #target sum for each parttion

        dp = [False] * (target+1) #initilise dpa rray for 0/1 knapsack
        dp[0] = True #base case, sum 0 is always true

        for num in nums:

            for i in range(target, num-1, -1): #go backwards and use every no once
                if dp[i-num]:
                    dp[i] = True

        return dp[target]