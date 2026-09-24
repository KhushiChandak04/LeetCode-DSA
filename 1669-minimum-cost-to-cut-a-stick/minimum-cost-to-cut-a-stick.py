class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        cuts.append(0)
        cuts.append(n) #add 2 ends of the stick

        cuts.sort() #sort all the cut positions in ascending order
        m = len(cuts)

        dp = [[0] * m for _ in range(m)]

        #we start from -3 because we need atleast one position between i and j
        for i in range(m-3, -1, -1):
            for j in range(i+2, m):

                dp[i][j] = float('inf') #start with a very large number here
                
                for k in range(i+1, j): #every possible cut between i and j is k
                    dp[i][k] #cost of cutting left part
                    dp[k][j] #cost of cutting right part

                #from cuts i to cuts j
                    cuts[j] - cuts[i]

                #total cost if k is the last cut
                    cost = dp[i][k] + dp[k][j] + cuts[j] - cuts[i]

                #keep the smaller cost
                    dp[i][j] = min(dp[i][j], cost)

        return dp[0][m-1] #this is the whole stick from 0 to n