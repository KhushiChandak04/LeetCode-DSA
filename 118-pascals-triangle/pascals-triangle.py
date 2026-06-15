class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            row = [1] * (i+1) #row setup iteration of elements per row
            for j in range(1, i):
                row[j] = result[i-1][j-1] + result[i-1][j] 
#curr element = left above element + right above element
            result.append(row)
        return result