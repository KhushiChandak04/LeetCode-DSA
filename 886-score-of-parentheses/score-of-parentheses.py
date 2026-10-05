class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
        depth = 0 #initilse how deeply nested the brace is

        for i in range(len(s)):
            if s[i] == '(': #opeining brace
                depth += 1
            else:
                depth -= 1
            #if it is a pair ():
                if s[i-1] == '(':
                    score += 2 ** depth

        return score