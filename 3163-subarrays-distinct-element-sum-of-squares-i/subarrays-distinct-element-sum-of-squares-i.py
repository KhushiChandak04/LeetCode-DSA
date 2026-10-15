class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            seen = set()
            for j in range(i, len(nums)):
                #add curr element
                seen.add(nums[j])
                count = len(seen)

                ans += count*count
        return ans