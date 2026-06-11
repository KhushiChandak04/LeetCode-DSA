class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if low % 2 != 0 or high % 2 != 0:
            return (high - low) // 2 + 1 #odd difference b/w high and low
        else:
            return (high - low) // 2 #even difference b/w high and low