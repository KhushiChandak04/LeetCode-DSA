class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #area = height * width
        stack = []
        ans = 0

        heights.append(0) #extra 0 to process remaining bars
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]: #if current bar is smaller than the bar at the top of the stack, we calculate the area
                h = heights[stack.pop()] #height of the recttangle
                if not stack:
                    w = i #width = i
                else:
                    w = i - stack[-1] -1 #rectangle starts after stack [-1] #or the top of the stack
                area = w*h
                ans = max(ans, area)

            stack.append(i) #put current bar's index in the stack
        return ans