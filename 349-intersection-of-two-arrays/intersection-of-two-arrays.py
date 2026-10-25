class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        seen = [False] * 1001
        for num in nums1: #mark nums present in nums1
            seen[num] = True
        
        ans = []

        for num in nums2:
            if seen[num]:
                ans.append(num)
                seen[num] = False #to keep a check on duplicates
        return ans