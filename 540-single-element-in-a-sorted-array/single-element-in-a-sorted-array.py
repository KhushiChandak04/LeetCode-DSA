class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 2 ptr approach as complexity has to be O(log n)
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1: #check if mid is even
                mid -= 1
            #check if every pair is complete
            if nums[mid] == nums[mid+1]:
                #pair is complete
                left = mid + 2 #ignore this pair and move ahead
            else:
                right = mid
        return nums[left]