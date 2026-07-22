class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)

        small_part = nums[:(n+1) // 2] #small nos till mid pt after sort
        large_part = nums[(n+1) // 2:]

        #fill even indices like 0,2,4.. with smaller half
        nums[::2] = small_part[::-1] #(start:end:step) format
        #fill odd indices with larger half
        nums[1::2] = large_part[::-1] #in reverse order