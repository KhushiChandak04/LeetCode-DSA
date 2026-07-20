class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #add id smaller val after current, otherwise subtract
        values = {
            #make a dictionary with key:value pairs
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        ans = 0 #initilise

        for i in range(len(s)):
            #if next val is bigger, subtract
            if i < len(s) - 1 and values[s[i]] < values[s[i+1]]: #we also chk if the next character exists or not, otherwise it will move out of index
                ans -= values[s[i]]
            else:
                ans += values[s[i]]
        return ans