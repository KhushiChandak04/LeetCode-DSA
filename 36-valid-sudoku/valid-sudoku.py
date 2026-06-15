class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = set() #initialise into grps
        cols = set()
        boxes = set()

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".": #partially filled sudoku
                    continue
                if (r, num) in rows: #since we are iterating 1-9 nos so if another is put there the sudoku becomes invalid, checking for duplicates
                    return False
                if (c, num) in cols:
                    return False
                if ((r // 3, c // 3), num) in boxes:
                    return False

                #stores current number
                rows.add((r, num))
                cols.add((c, num))
                boxes.add(((r // 3, c // 3), num))
        return True