class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        rows = len(heights)
        cols = len(heights[0])
        result = []

        # check every cell here we are using simple dfs soln
        for r in range(rows):
            for c in range(cols):

                # visited set for Pacific
                pacific = self.canReachPacific(heights, r, c, set())
                # visited set for Atlantic
                atlantic = self.canReachAtlantic(heights, r, c, set())
                # if it can reach both then
                if pacific and atlantic:
                    result.append([r, c])

        return result


    def canReachPacific(self, heights, r, c, visited):  # it is left and top edges

        rows = len(heights)
        cols = len(heights[0])

        # if we reach top row or left column, its pacific reached
        if r == 0 or c == 0:
            return True

        # if we already visited this cell, stop
        if (r, c) in visited:
            return False

        # mark this cell as visited
        visited.add((r, c))

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:  # check all 4 directions

            nr = r + dr  # new row
            nc = c + dc  # new col

            # check boundaries
            if 0 <= nr < rows and 0 <= nc < cols:
                # water can flow from current cell to neighbor
                if heights[nr][nc] <= heights[r][c]:
                    # check if neighbor can reach Pacific
                    if self.canReachPacific(heights, nr, nc, visited):
                        return True
        return False


    def canReachAtlantic(self, heights, r, c, visited):  # it is right and bottom edges

        rows = len(heights)
        cols = len(heights[0])

        # if we reach bottom row or right column, its Atlantic reached
        if r == rows - 1 or c == cols - 1:
            return True
        # if we already visited this cell, stop
        if (r, c) in visited:
            return False
        # mark this cell as visited
        visited.add((r, c))

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:  # check all 4 directions
            nr = r + dr  # new row
            nc = c + dc  # new col
            # check boundaries
            if 0 <= nr < rows and 0 <= nc < cols:
                # water can flow from current cell to neighbor
                if heights[nr][nc] <= heights[r][c]:
                    # check if neighbor can reach Atlantic
                    if self.canReachAtlantic(heights, nr, nc, visited):
                        return True

        return False