class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        reverse = alphabet[::-1]
        ans = ""
        for word in words:
            total = 0
            for ch in word:
                total += weights[alphabet.index(ch)]
            ans += reverse[total % 26]
        return ans