class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0 #we can use simple sliding window here
        zeroes = 0
        ans = 0

        for right in range(len(nums)):

            if nums[right] == 0: #if 0 encountered incr its count
                zeroes += 1

            while zeroes > k: #if zeroes are more than k, shrink the window

                if nums[left] == 0: #if left element is 0, decrease zero count
                    zeroes -= 1

                left += 1

            length = right - left + 1
            if length > ans:
                ans = length

        return ans