class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #For each number in nums1, we go to nums2 and ask: "What is the first bigger number to the right of this number?" thats next greater element

        stack = [] #stores nums for which we havent found a bigger num yet
        ans = {} #simply stores the answers we found

        for num in nums2:
            while stack and num > stack[-1]:
                ans[stack.pop()] = num
            stack.append(num)
        
        while stack:
            ans[stack.pop()] = -1 #no number is greater
        
        result = []
        for num in nums1:
            result.append(ans[num])
        return result