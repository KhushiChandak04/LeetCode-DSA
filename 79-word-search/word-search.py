class Solution(object):
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c, index):
            if index == len(word): #base case
                return True
            if (r<0 or r>=rows or c<0 or c>=cols or board[r][c] != word[index]): #boundary cases and if word is not present only
                return False
            temp = board[r][c] #mark visited
            board[r][c] = "#" #to avoid revisits
            
            found = (
                dfs(r+1, c, index+1) or
                dfs(r-1, c, index+1) or
                dfs(r, c+1, index+1) or
                dfs(r, c-1, index+1)
            ) #check all 4 directions
            
            board[r][c] = temp #backtrack
            return found

        for r in range(rows): #recursive final function
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False