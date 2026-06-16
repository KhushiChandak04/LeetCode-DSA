class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        result = [] #make a stack
        for ch in s:
            if ch.isalpha(): #handles string inputs
                result.append(ch)
            elif ch == '*':
                if result:
                    result.pop()
            elif ch == '#':
                result.extend(result) #repeats
            else: #for #
                result.reverse()
        return "".join(result)