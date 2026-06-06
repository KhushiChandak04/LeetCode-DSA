class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): #check their lengths
            return False
        if sorted(s) == sorted(t): #sorted versions same or not
            return True
        return False