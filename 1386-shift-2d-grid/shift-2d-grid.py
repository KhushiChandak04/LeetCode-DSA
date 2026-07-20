class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])

        #answer grid
        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                index = i * n + j #current index in 1-D
                new_index = (index + k) % (m*n) #after 1-d shift, as index is 0 after 9th shift
                #convert back to 2-d
                new_row = new_index // n
                new_col = new_index % n
                ans[new_row][new_col] = grid[i][j]

        return ans