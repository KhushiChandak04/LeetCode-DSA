class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [""] #empty stack to store strings
        for ch in s:
            if ch == '(':
                stack.append("") #if opening bracket encountered, start a new string
            elif ch == ')':
                word = stack.pop()
                word = word[::-1] #if closing, then reverse the current string
                stack[-1] += word #add revversed word to prev string
            else:
                stack[-1] += ch #if its a normal letter

        return stack[0]