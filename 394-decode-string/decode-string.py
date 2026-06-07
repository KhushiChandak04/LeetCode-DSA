class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        string = ""
        number = 0 #initialise all
        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch == '[':
                stack.append((string, number))
                string = ""
                number = 0
            elif ch == ']':
                oldString, repeat = stack.pop()
                string = oldString + repeat * string
            else:
                string += ch
        return string