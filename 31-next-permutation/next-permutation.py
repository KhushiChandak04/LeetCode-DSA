class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = n-2 #always 2nd last element
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]: #checks last element is smaller than the one to its right
            pivot -= 1 #shift pivot to its right
        if pivot >= 0:
            right = n-1
            while nums[right] <= nums[pivot]: #number just immediately greater than pivot
                right -= 1 #shift right to the left position
            nums[pivot], nums[right] = nums[right], nums[pivot] #swap
        left = pivot + 1 #shift left to next of pivot
        right = n - 1 #right to last

        while left < right: #until both ptrs meet
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
#1. Scan from right → find pivot
#2. Scan from right → find just larger number
#3. Swap
#4. Reverse suffix