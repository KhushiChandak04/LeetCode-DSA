class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        for i in range(1, rows):
            grid[i][0] = grid[i][0] + grid[i-1][0] #to pick or not to pick
        for j in range(1, cols):
            grid[0][j] = grid[0][j] + grid[0][j-1]

        for i in range(1,rows):
            for j in range(1,cols):
                grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1]) #choose minimum from top and left
        return grid[rows-1][cols -1]