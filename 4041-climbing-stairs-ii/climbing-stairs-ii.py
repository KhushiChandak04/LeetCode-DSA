class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        dp = [float('inf')] * (n+1) #initilise it to maximum possible value
        dp[0] = 0 #base case

        for i in range(1,n+1): #chk every step from 1 to n+1
            for j in range(1,4): #can jump onli 1,2,3,4 steps at a time

                if i-j >= 0: #chk if jump possible
                    total = dp[i-j] + costs[i-1] + j*j #cost -1 as array is 0 indexed + cost of step is j*j
                    if total < dp[i]:
                        dp[i] = total #keep the minimum cost here
        return dp[n]