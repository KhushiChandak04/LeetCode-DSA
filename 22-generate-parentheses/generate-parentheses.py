class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        def backtrack(current, open_bracket, close_bracket):
            if len(current) == 2*n: #we have used all combos
                answer.append(current)
                return
            if open_bracket < n: # add '(' if we still have some left
                backtrack(current + '(', open_bracket + 1, close_bracket)

            if close_bracket < open_bracket: #add close bracket onli if it has unmatched bracket here
                backtrack(current + ')', open_bracket, close_bracket + 1)
                
        backtrack("", 0, 0)
        return answer