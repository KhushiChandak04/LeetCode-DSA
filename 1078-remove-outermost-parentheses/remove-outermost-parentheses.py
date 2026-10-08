class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = ""
        depth = 0

        for ch in s:
            if ch == '(':
                if depth > 0:
                    answer += ch
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    answer += ch
        return answer