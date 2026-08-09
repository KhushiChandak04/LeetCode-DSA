class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        even = 0 #initilise
        odd = 0

        for i in range(len(piles)):
            if i % 2 == 0:
                even += piles[i]
            else:
                odd += piles[i]
        return True