class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        #store which numbers are already used in each row
        rows = [[False] * 10 for _ in range(9)]

        #store which numbers are already used in each col
        cols = [[False] * 10 for _ in range(9)]

        #store which numbers are already used in each 3x3 box
        boxes = [[False] * 10 for _ in range(9)]

        #store all empty cells
        empty = []


        #go through the whole board once
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.': #empty cell
                    #store this empty cell
                    empty.append((row, col))

                else:
                    #convert character into number
                    num = int(board[row][col])
                    #find which 3x3 box this cell belongs to
                    box = (row // 3) * 3 + (col // 3)
                    #mark number as already used
                    rows[row][num] = True
                    cols[col][num] = True
                    boxes[box][num] = True

        def solve(index):
            #if all empty cells are filled
            if index == len(empty):
                return True
            #get the current empty cell
            row, col = empty[index]
            #find its 3x3 box
            box = (row // 3) * 3 + (col // 3)

            #try nums from 1-9
            for num in range(1, 10):
                #check if number is already used
                if rows[row][num]:
                    continue
                if cols[col][num]:
                    continue
                if boxes[box][num]:
                    continue
                #place the number there
                board[row][col] = str(num)

                #mark number as used
                rows[row][num] = True
                cols[col][num] = True
                boxes[box][num] = True
                #try solving the next empty cell
                if solve(index + 1):
                    return True

                #if it did not work then undo the action
                board[row][col] = '.'

                rows[row][num] = False
                cols[col][num] = False
                boxes[box][num] = False

            #no number worked for this cell
            return False
        #start solving from the first empty cell
        solve(0)