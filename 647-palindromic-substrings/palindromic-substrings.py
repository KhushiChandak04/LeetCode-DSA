class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0 #initialise
        for i in range(len(s)):

            #odd lenght palindrome
            left = i #set ptrs
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            #even length palindrome
            left = i
            right = i + 1 #set prts
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count