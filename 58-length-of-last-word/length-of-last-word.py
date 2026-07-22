class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) -1
        while s[i] == " ":
            i -= 1 #skip trailing spaces

        length = 0 #initilise
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length