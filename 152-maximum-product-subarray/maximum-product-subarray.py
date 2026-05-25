class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        prefix, suffix = 1,1 #initialise to 1 as it is product
        ans = float('-inf')

        for i in range (n):
            if prefix == 0:
                prefix = 1  #resets to 1 if encountered a 0
            if suffix == 0:
                suffix = 1  #ressts to 1 again similarly

        #main logic in i block
            prefix *= nums[i] # Multiply prefix with front element
            suffix *= nums[n - i - 1] # Multiply suffix with back element
            ans = max(ans, prefix, suffix)
            
        return ans