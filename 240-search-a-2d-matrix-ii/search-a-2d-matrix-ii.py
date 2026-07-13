class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols - 1 #two ptrs

        while row < rows and col >= 0: #start from top right corner

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target: #move left as elements there are smaller
                col -= 1
            
            else: #otherwise move right
                row += 1
        return False