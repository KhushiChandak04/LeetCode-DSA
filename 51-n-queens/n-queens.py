class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        answer = []
        board = [] #create and empty board here

        for i in range(n):
            board.append(["."] * n) #here make a blank board with dots, make string
        
        def isSafe(row, col): #check whether placing this queen is safe or not
            for i in range(row):
                if board[i][col] == "Q":
                    return False #dont place queen there if it is in same col, so not safe

            # 1. Check upper left diagonal
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # 2. Check upper right diagonal
            i = row - 1 
            j = col + 1
            
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1 #traverse ahead
                j += 1 # Fixed: upper right moves right (+1)
                
            return True #alternate case if no queen is there as above
        
        def backtrack(row): #make a new function to remove the placements of queens
            if row == n: #check if all queens are placed correctly
                temp = []
            #convert every row to a string manually
                for r in board:
                    s = ""
                    for ch in r: # Fixed: loop through row 'r', not empty string 's'
                        s += ch
                    temp.append(s) #saved to string the converted one
                answer.append(temp) #now saved the string to answer
                return
            #actually placing the queens here
            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = "Q" #if the position is fine add a queen there

                    backtrack(row + 1) #recurse to next row
                    board[row][col] = "." #to pop and undo the queen placed
        backtrack(0)
        return answer