class Solution(object):
    def rob(self, nums):
        #initialise two pointers
        prev = 0
        prev2 = 0
        for i in nums:
            pick = prev2 + i #fox max sum
            notPick = prev #for not picking adjacent
            current = max(pick, notPick)
            prev2 = prev #to move ahead
            prev = current
        return prev