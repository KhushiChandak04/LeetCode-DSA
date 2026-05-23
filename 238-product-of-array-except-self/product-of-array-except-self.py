class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [0] * n #initialise result with 0

        left_product = 1 # first pass of forward multiply of results
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        right_product = 1 #second pass is right to left
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        return result       