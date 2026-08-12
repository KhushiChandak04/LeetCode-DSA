class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #core idea - keep expanding the window, if any number appears more than k times, move left until it becomes valid again
        count = {}
        left = 0 #initilise the ptr
        ans = 0

        for right in range(len(nums)):
            if nums[right] not in count:
                count[nums[right]] = 0

            count[nums[right]] += 1 #moving right adds nos

            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1 #moving left removes nos

            ans = max(ans, right - left + 1)
        return ans