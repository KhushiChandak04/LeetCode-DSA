class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left_most = min(min_index, max_index) #left ptr
        right_most = max(min_index, max_index) #right ptr

        #we have 3 choices, either remove elements from left side to reach both min and max, or remove elements from right side to reach them or one each from left and right to reach them

        both_left = right_most + 1
        both_right = n - left_most
        one_each = (left_most+1) + (n-right_most)

        return min(both_left, both_right, one_each)