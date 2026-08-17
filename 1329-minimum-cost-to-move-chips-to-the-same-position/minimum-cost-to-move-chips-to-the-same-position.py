class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        odd = 0
        even = 0

        for pos in position:
            if pos % 2 == 0:
                even += 1
            else:
                odd += 1

        return min(odd, even) #move the smaller group