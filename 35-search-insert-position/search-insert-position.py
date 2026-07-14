class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #TO MAINTAIN O(logn) complexity, we will use 2 ptr approach
        left = 0
        right = len(nums) - 1

        while left <= right: #binary search
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left