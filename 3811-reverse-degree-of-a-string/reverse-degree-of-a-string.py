class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        answer = 0

        for i in range(len(s)):
            position = i+1 #as indexing starts from 0 in python
            value = 26 - alphabet.index(s[i])
            answer += position * value
        return answer