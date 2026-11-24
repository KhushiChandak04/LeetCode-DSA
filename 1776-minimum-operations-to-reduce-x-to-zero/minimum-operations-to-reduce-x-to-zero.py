class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        #sliding window problem
        n = len(nums)
        target = sum(nums) - x

        if target < 0: #if total sum is less than x, we cannot reduce x to 0
            return -1

        left = 0
        total = 0
        maxlen = 0

        for right in range(n):

            total += nums[right] # add current element

            # if sum becomes greater than target, shrink the window
            while total > target:
                total -= nums[left]
                left += 1

            # check if current window has the required sum
            if total == target:
                length = right-left+1

                if length > maxlen:
                    maxlen = length

        if maxlen == 0 and target != 0:
            return -1

        return n-maxlen #minimum operations = total elements - longest subarray