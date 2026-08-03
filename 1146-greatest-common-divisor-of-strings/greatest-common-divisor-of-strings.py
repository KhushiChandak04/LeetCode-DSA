class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1: #if both strings cannot be formed by same pattern
            return ""

        a = len(str1)
        b = len(str2)

        #find GCD of lengths
        while b:
            a, b = b, a % b
        return str1[:a]