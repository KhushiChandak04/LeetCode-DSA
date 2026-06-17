class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        low = 0 #initilise ptrs
        mid = 0
        high = n - 1

        while mid <= high:
            if nums[mid] == 0: #case 1 if current element is 0
                nums[low], nums[mid] = nums[mid], nums[low] #swap and placce 0 in its correct position
                low += 1
                mid += 1
            elif nums[mid] == 1: #case 2 if middle element is 1
                mid += 1 # 1 belongs correctly so just move mid there
            else: #case 3 if current element in middle is 2 then
                nums[high], nums[mid] = nums[mid], nums[high] #swap with high
                high -= 1 #dont move mid here, to shrink the last region