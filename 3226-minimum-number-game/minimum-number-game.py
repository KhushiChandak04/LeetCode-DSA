class Solution(object):
    def numberGame(self, nums):
        n = len(nums)
        nums.sort()
        arr = []
        for i in range (0, n, 2): #start,stop,setep size this format
            arr.append(nums[i+1])
            arr.append(nums[i])
        return arr