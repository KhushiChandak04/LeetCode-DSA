class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # bfs search as we need level by level traversal
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0  # initialise count

        # put all rotten oranges in queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0  # initialise
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q and fresh > 0:
            size = len(q)  # oranges rotten at current minute

            for i in range(size):
                r, c = q.popleft()  # pop current rotten orange

                for dr, dc in directions:  # change in row and change in col
                    nr = r + dr
                    nc = c + dc

                    # check if neighbour is inside grid and is fresh
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2      # make rotten
                        fresh -= 1
                        q.append((nr, nc))    # will rot others next minute

            minutes += 1

        return minutes if fresh == 0 else -1