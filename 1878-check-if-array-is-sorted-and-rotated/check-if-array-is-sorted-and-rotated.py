class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        count = 0 #no of circular drops for rotation

        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count += 1

                if count > 1: #if more than one break or drop, thats not a rotated array
                    return False
        return True