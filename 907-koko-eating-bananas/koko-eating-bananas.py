class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)

        while left < right:
            mid = (left+right) // 2
            hours = 0 #initilise
            for pile in piles:
                hours += (pile + mid - 1) // mid #ceiling div
            if hours <= h:
                right = mid
            else:
                left = mid+1
        return left