class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
# strategy used : fix first number -> fix 2nd number -> find remaining 2 nos. with left and right pointers
        nums.sort()
        ans = [] #for storing final ans
        n = len(nums)

        for i in range(n - 3):
            #skip duplicate 1st no
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                #skip 2nd duplicate number
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j+1
                right = n-1 #set ptr position here

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        ans.append([
                            nums[i], nums[j], nums[left], nums[right]
                        ])
                        left += 1 #traverse ptrs ahead
                        right -=1

                        #skip duplicates here
                        while left < right and nums[left] == nums[left -1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -=1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return ans