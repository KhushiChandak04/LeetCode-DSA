class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #core idea = 

        dp = [0] * (n+1) #initilise a blank dp
        dp[0] = 1 #base case of empty tree
        dp[1] = 1 #one node

        for nodes in range(2, n+1): #iterate with 2 as we have 2 base cases
            for root in range(1, nodes+1): #treat every node as root
                left = root - 1 #no. of nodes on left
                right = nodes - root #no of nodes on right
                dp[nodes] += dp[left] * dp[right] #combinations total
        return dp[n]