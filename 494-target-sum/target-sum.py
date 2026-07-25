class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # sum +ve - sum -ve = target AND sum +ve + sum -ve = total_sum
        total_sum = sum(nums)
        #check edge cases
        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0
        #subset = how many nos can make target
        subset_sum = (total_sum + target) // 2
        #dp stores the ways to fulfil the sum
        dp = [0] * (subset_sum + 1)
        dp[0] = 1 #base case as only 1 way to get sum 0 empty set

        for num in nums:
            for j in range(subset_sum, num -1, -1): #traverse reverse to avoid overwriting vals
                dp[j] += dp[j-num]
        return dp[subset_sum]