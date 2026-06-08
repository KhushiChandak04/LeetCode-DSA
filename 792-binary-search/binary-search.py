class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0 #ptrs
        high = n-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif target >= nums[mid]: #search in right half
                low = mid + 1
            else: #search in left half
                high = mid - 1
        return -1