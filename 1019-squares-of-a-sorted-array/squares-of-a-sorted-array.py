class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #since the array is alrd sorted, we can use the 2ptr approach
        n = len(nums)
        left = 0
        right = n-1

        ans = [0] * n #store the sorted squares here
        i = n-1 #start filling ans arr frm right end

        while left <= right:

            #check which number has bigger absolute value as it will have a larger square
            if abs(nums[left]) > abs(nums[right]):
                ans[i] = nums[left] * nums[left] #square the larger val
                left += 1
            else:
                ans[i] = nums[right] * nums[right]
                right -= 1
                
            i -= 1
        return ans