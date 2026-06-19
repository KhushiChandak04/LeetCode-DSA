class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1 #same as prev majority element
        ans = []
        for i in freq:
            if freq[i] > len(nums) // 3: #just div by 3 this time
                ans.append(i)
        return ans