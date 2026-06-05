class Solution(object):
    def spiralOrder(self, matrix):
        result = []
        top = 0 #initialise ptrs boundary positions
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while left <= right and top <= bottom: #until boundaries are valid
            #left to rigt we move 1st pass
            for i in range (left, right+1):
                result.append(matrix[top][i]) #appends top row
            top += 1
            #right to bottom we move 2nd pass
            for i in range (top, bottom+1):
                result.append(matrix[i][right]) #appends right column
            right -= 1
            #for bottom to top remaining rows:
            if top <= bottom:
                for i in range(right, left-1 , -1): #bottom row
                    result.append(matrix[bottom][i])
                bottom -= 1
            #for left to right remaining cols:
            if left <= right:
                for i in range(bottom, top -1, -1): #left col
                    result.append(matrix[i][left])
                left += 1
        return result