class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] #stores opening braces and pops them when corresponding closed braces
        for ch in s: #check of opening braces in given str
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
            #check for matching pair
                if (ch == ')' and top == '(') or \
                    (ch == '}' and top == '{') or \
                    (ch == ']' and top == '['):
                    continue
                else:
                    return False
        return not stack