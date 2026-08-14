class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {} #dictionary to initilise the soln
        left = 0
        ans = 0 #initilise

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1 #increase count of current character
            while count[s[right]] > 2:
                count[s[left]] -= 1 #remove left character from the window
                left += 1 #move ahead the left ptr

            ans = max(ans, right - left + 1) #update maximum window lwngth
        return ans