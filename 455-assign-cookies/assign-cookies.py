class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        cookie = 0 #ptr initialise
        child = 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]: #current cookie satisfies current child
                child += 1
            cookie += 1 #cookie too small so discard it and move on to the next
        return child