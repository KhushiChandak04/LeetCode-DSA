class Solution(object):
    def maxSubArray(self, nums):
        max = float('-inf')
        sum = 0
        for i in range (len(nums)):
            sum += nums[i]
            if sum > max:
                max = sum
            if sum < 0:   #keep extending the sub array till sum is +ve, discard sum if it becomes negative and start from sum = 0 and start fresh again
                sum = 0
        return max