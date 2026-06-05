class Solution(object):
    def setZeroes(self, matrix):
## First mark all original 0s, then update matrix; otherwise newly created 0s will cause wrong changes.
        m = len(matrix) #define size of matrix m x n
        n = len(matrix[0])
        row = [0] * m #just markers as we directly cant make it 0, because we have to traverse it first so we feed it into dummy matrix
        col = [0] * n
        for i in range (m):
            for j in range (n):
                if matrix[i][j] == 0: #if element is 0. just mark its row and col as 0
                    row[i] = 1
                    col[j] = 1
        for i in range (m):
            for j in range (n):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0