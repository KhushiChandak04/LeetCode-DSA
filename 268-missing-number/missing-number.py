class Solution(object):
    def missingNumber(self, nums):
        n = len(nums) + 1 #as target has one missing number, so it has one less
        hashset = set(nums)  #store all current elements in a hashset as a list
        for i in range (0, n+1):
            if i not in hashset:
                return i
        return -1