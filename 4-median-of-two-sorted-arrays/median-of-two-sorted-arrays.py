class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        i = 0 #two ptrs used to merge nos in ascending order of the arrays
        j = 0

        while i < len(nums1) and j < len(nums2):
            
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

    #append remaining nos
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        n = len(merged)
        
        if n % 2 == 1: #odd no of digits
            return float(merged[n // 2])
        return (merged[n // 2] + merged[n // 2 - 1]) / 2.0