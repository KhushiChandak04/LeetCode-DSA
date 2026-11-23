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

            if nums[right] == 0: #what to do if 0 is encountered
                if zeroes < k:
                    zeroes += 1 #we can still transform a 0
                else:
                    while nums[left] != 0: #keep sliding window until one zero leaves the window
                        left += 1
                    left += 1
            length = right-left+1
            
            if length > ans:
                ans = length
        return ans