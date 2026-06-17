class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #Start from the back because the empty spaces are at the back, making it safe to place the largest remaining element without losing data.
        
        i = m - 1 #last valid element in nums1
        j = n - 1 #last valid element in nums2
        k = m + n - 1 #last position in merged array

        while i >= 0 and j >= 0: #merge while both arrays have elements
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i] #place larger element at the end
                i -= 1 #shift to left side as we were at the end of array at the beginning
            else:
                nums1[k] = nums2[j]
                j -= 1 #same
            k -= 1
        while j >= 0: #nums2 still has values
            nums1[k] = nums2[j]
            j -= 1
            k -= 1