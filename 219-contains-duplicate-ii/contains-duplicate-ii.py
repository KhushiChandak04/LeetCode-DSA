class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:

                if i - seen[nums[i]] <= k: #given condition
                    return True

            seen[nums[i]] = i #update the latest
        return False