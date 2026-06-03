class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        size = n * n #given size
        hash = [0] * (size + 1) #blank hash initialise of 2D
        for row in grid:
            for num in row:
                hash[num] += 1 #increase count of current number cuz indexing starts from 0
        repeating = -1
        missing = -1
        for i in range(1, size + 1):
            if hash[i] == 2:
                repeating = i
            elif hash[i] == 0:
                missing = i
        return [repeating, missing]