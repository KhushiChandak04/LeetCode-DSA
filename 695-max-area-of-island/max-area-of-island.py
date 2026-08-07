class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            #outside grid or is water then the case is 0
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            #mark current land as visited
            grid[r][c] = 0
            area = 1 #initilise counter

            #explore all 4 directions
            area += dfs(r+1, c) #right
            area += dfs(r-1, c) #left
            area += dfs(r, c+1) #top
            area += dfs(r, c-1) #bottom

            return area

        maxArea = 0 #initilise
        #visit every cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c))
        return maxArea