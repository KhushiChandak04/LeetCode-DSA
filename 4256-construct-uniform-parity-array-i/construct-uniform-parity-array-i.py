class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        has_odd = False
        for nums in nums1:
            if nums % 2 == 1:
                has_odd = True
        return True