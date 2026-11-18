class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        ans = ""

        for i in range(len(values)):
            while num >= values[i]: #add character corresp to number if it exceeds it

                ans += symbols[i]
                num -= values[i]

        return ans