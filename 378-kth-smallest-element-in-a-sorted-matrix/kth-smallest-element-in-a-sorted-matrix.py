class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        #we use binary search for the most efficient complexity here, and elements are already sorted here so this is the best

        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n-1][n-1]

        while left < right:
            mid = (left+right) // 2
            count = 0
            row = n-1
            col = 0
            #count how many elements are <= mid

            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            #chk binary search range
            if count < k:
                left = mid + 1
            else:
                right = mid
                
        return left