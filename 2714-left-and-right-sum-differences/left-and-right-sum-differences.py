class Solution(object):
    def leftRightDifference(self, nums):
        totalsum = sum(nums) #sum of whole array
        leftsum = 0 #initialise it to some value
        ans = []
        for i in range(len(nums)):
            rightsum = totalsum - leftsum - nums[i]
            ans.append(abs(leftsum - rightsum)) #appends absolute value here
            leftsum += nums[i] 
        return ans