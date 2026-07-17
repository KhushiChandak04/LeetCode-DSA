class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1): #possible starting position
            #compare characters
            if haystack[i: i+m] == needle:
                return i #return the index position
        return -1