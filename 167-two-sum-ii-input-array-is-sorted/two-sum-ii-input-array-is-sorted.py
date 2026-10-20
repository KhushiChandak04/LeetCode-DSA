class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) -1 #start from both the ends

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left+1, right+1] #as indexing starts from 0

            elif total < target:
                left += 1 #if sum is too small we move left fwd
            else:
                right -= 1