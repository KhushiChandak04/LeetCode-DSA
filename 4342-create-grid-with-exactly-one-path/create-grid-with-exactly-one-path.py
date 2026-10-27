class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid = [['#'] * n for i in range(m)] #make the whole grid blocked

        for j in range(n): #make the first row free
            grid[0][j] = '.'

        for i in range(m): #make the last col free
            grid[i][n-1] = '.' #given that last row is n-1
        
        ans = [] #convert each row to a string
        for i in range(m):
            row = ""
            for j in range(n):
                row += grid[i][j]
            ans.append(row)
        return ans