class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n #to reduce unnecessary repeated rotations for larger k value
        nums.reverse() #reverse full array

        #reverse first k elements
        nums[:k] = nums[:k][::-1]
        #reverse remaining elements
        nums[k:] = nums[k:][::-1]