class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False #both strings have to be of same length
        if goal in s+s: #we add s twice to chk if the order is present there, linear complexity
            return True
        return False