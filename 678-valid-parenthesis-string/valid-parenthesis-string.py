class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        #minimum and maximum possible open brackets
        minimum = 0
        maximum = 0

        for ch in s:

            if ch == '(':
                minimum += 1
                maximum += 1

            elif ch == ')':
                minimum -= 1
                maximum -= 1

            #if *
            else:
                minimum -= 1
                maximum += 1

            #minimum open brackets cannot be negative
            if minimum < 0:
                minimum = 0

            #even the maximum possible brackets went negative
            if maximum < 0:
                return False

        #if we can have exactly 0 open brackets, it is valid
        return minimum == 0