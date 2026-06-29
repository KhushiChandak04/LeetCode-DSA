class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height) #no. of elevations
        left = 0
        right = n - 1 #ptrs
        leftmax = 0 #highest height as seen from left
        rightmax = 0 #highest height as seen from right
        waterstored = 0

        while left < right:
            if height[left] < height[right]: #if left wall is smaller
                if height[left] >= leftmax: #update max height on left side
                    leftmax = height[left]
                else:
                    waterstored += leftmax - height[left] #water trapped at current position
                left += 1 #move left ptr
            else: #if right wall is smaller or equal
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    waterstored += rightmax - height[right] #water trapped at current position
                right -= 1
        return waterstored