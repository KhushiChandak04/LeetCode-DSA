class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0 #to place a valid element

        for i in range(len(nums)):
            if nums[i] != val: #if current element is to be kept
                nums[k] = nums[i]
                k += 1
        return k