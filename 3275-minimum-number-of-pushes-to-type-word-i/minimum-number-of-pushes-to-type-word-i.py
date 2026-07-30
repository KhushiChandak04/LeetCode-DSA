class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        pushes = 0 #initilise
        for i in range(len(word)):
            #first 8 letters - 1 push, next 8 letters 2 push, next 8 letters 3 push etc etc
            pushes += (i // 8) + 1
        return pushes