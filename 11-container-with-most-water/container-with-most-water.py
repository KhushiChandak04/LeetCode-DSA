class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1 #initialise 2 ptrs from left and right sides
        max_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            max_area = max(max_area, current_area)

            #for updating pointers moving ahead 
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area