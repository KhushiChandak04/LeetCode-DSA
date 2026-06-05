class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
#step 1 - take transpose of matrix i.e. swap the positions
        for i in range (n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#step 2 - reverse the rows content
        for i in range (n):
            matrix[i].reverse()