class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Use DFS to visit every 1 and change it to 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            #outside grid
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            #if water or already visited -> convert to 0 all the visited
            if grid[row][col] == "0":
                return
            #mark cuurent as visited
            grid[row][col] = "0"

            #visit all 4 directions
            dfs(row - 1, col) #up
            dfs(row + 1, col) #down
            dfs(row, col - 1) #left
            dfs(row, col + 1) #right
        
        islands = 0 #initilise
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        return islands