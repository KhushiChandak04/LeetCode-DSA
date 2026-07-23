class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            stones.sort()
            y = stones.pop() #largest
            x = stones.pop() #second largest
            if y != x:
                stones.append(y - x)
        return stones[0] if stones else 0