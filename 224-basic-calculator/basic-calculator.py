class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        #use stack here
        result = 0 #initilise
        number = 0 #to convert string to no
        sign = 1 # +ve= 1 or -ve = -1
        stack = []

        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            if ch == '+':
                result += sign * number
                number = 0
                sign = 1
            elif ch == '-':
                result += sign * number
                number = 0
                sign = -1
            elif ch == '(':
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1
            elif ch == ')':
                result += sign * number
                number = 0
                
                result *= stack.pop() #sign before (
                result += stack.pop() #result after (
        result += sign * number
        return result