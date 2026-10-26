class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left = 0
        right = len(s) - 1

        #check characters from both ends
        while left < right:

            #skip non-alphanumeric characters from left
            if not s[left].isalnum():
                left += 1
                continue

            #skip non-alphanumeric characters from right
            if not s[right].isalnum():
                right -= 1
                continue

            #compare characters ignoring uppercase/lowercase
            if s[left].lower() != s[right].lower():
                return False

            #move both pointers
            left += 1
            right -= 1

        return True