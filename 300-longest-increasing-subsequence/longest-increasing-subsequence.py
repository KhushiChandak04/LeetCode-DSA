class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        n = len(nums)
        dp = list() #temporaty to store increasing subsequence

        for i in range (n):
            #if current element is greater than last element,
            #extend increasing subsequence

            if not dp or nums[i]>dp[-1]:  #smaller ending is better
                dp.append(nums[i])
            else:
                #binary search to replace
                left = 0
                right = len(dp)-1 #both ptrs

                while left<=right:
                    mid = (left+right)//2

                    if dp[mid] < nums[i]:
                        left = mid + 1
                    else:
                        right = mid -1

                #replace with smaller value for better future subsequences
                dp[left] = nums[i]
        return len(dp)