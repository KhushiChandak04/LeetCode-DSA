class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #two ptr approach
        i = 0 #ptr for s
        j = 0 #ptr for t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1 #move ptrs if they match
        return i == len(s)