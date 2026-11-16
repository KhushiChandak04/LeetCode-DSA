class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            ans = ""

            for i in range(0, len(s), k): #take k characters at a time

                total = 0

                for j in range(i, i + k): #add the digits of the group
                    if j < len(s):
                        total += int(s[j])

                ans += str(total) # add the sum to the answer
            s = ans

        return s