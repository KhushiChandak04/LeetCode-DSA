class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(1, rows):
            for j in range(1,cols):
                if matrix[i][j] != matrix[i-1][j-1]: #compare with top left diagonal element
                    return False
        return True