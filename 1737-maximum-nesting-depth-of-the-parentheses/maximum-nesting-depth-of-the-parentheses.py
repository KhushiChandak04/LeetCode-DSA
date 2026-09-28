class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0 #current number of open braces
        ans = 0 #final answer

        for ch in s:
            if ch == '(':
                depth += 1
                ans = max(ans, depth)
            elif ch == ')':
                depth -= 1 #ifclosing brace found reduce depth
        return ans