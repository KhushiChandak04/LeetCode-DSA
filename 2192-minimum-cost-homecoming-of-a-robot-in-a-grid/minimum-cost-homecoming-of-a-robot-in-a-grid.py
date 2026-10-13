class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        #robot just needs to move from its starting position to its home.. we pay the cost of the cell we enter, not the cell we leave

        ans = 0 #initilise

        startRow = startPos[0] #starting and home pos
        startCol = startPos[1]
        homeRow = homePos[0]
        homeCol = homePos[1]

        #move up or down to reach home row
        if startRow < homeRow: #move up in this case
            for i in range(startRow+1, homeRow +1):
                ans += rowCosts[i] #we add row cost as row is onli changing col is the same while going up
        else:
            for i in range(startRow-1, homeRow-1, -1): #move down in this case
                ans += rowCosts[i] #same logic of adding row cost
        
        #move left or right to reach home col
        if startCol < homeCol:
            for i in range(startCol+1,homeCol+1):
                ans += colCosts[i] #we add col cost as row remains same while goin left or right
        else:
            for i in range(startCol-1, homeCol-1, -1):
                ans += colCosts[i] #samee logic of adding col cost
        
        return ans