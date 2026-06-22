class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        return min(
            text.count('b'),
            text.count('a'),
            text.count('l') // 2, #l appears twice
            text.count('o') // 2, #o appears twice
            text.count('n')
        )