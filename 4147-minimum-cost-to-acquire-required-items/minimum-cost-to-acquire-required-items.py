class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        #find out how many items can satisfy both the requirements
        both = min(need1, need2)
        total = both * min(costBoth, cost1+cost2) #choose the cheaper one

        need1 -= both #calculate remaining
        need2 -= both

        total += need1*cost1
        total += need2*cost2 #for remaiing, individual item cost is added
        total2 = costBoth * max(need1+both, need2+both) #if just buying type 3 is cheaper

        return min(total, total2)