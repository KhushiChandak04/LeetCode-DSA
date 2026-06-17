class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length = 0

        for ch in s: #Problem 1 code exact same logic
            if ch.isalpha():
                length += 1
            elif ch == '*':
                if length:
                    length -= 1
            elif ch == '#':
                length *= 2
            else:
                pass

        if k >= length: #but same for reverse
            return '.'

        for ch in reversed(s): #hard part
            if ch.isalpha():
                if k == length - 1:
                    return ch
                length -= 1
            elif ch == '*':
                length += 1
            elif ch == '#':
                length //= 2
                k %= length
            elif ch == '%':
                k = length - 1 - k

        return '.'