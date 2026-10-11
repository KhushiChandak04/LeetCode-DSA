class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = -1
        last = -1 #initilise ptrs before the start of array

        #find first occurance here
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            
            if nums[mid] == target:
                first = mid
                right = mid-1 #search further left

            elif nums[mid] < target:
                left = mid+1
            
            else:
                right = mid-1
    
    #find last occurance
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                last = mid
                left = mid+1 #search further right
            
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        
        return [first,last]