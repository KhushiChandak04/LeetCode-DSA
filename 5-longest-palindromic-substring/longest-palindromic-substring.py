class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
## whole string palindrome?
# compare from both ends
# longest palindrome substring?
# start from center and expand
# palindrome grows outward from its center
        ans = ""
        #odd length palindromic substring
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(ans):
                    ans = s[left:right+1]
                left -= 1
                right += 1
        #even length palindrome
        for i in range(len(s)):
            left = i
            right = i+1
            while left >=0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(ans):
                    ans = s[left:right+1]
                left -= 1
                right += 1
        return ans