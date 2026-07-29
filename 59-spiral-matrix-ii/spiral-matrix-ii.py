class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        #boundary
        top = 0
        bottom = n-1
        left = 0
        right = n-1
        num = 1 #start filling from 1

        while left <= right and top <= bottom:
            #fill top row left -> right
            for col in range(left, right +1):
                matrix[top][col] = num
                num += 1
            top += 1

            #fill right col top -> bottom
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            #fill bottom row right -> left
            for col in range(right, left -1, -1): #-1 as reverse order
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

            #fill left col bottom -> top
            for row in range(bottom, top -1, -1): #-1 as reverse order
                matrix[row][left] = num
                num += 1
            left += 1
            
        return matrix