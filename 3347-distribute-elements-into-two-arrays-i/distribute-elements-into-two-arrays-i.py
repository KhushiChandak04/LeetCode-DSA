class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1 = [nums[0]] #first element always goes to arr1
        arr2 = [nums[1]] #second element always goes to arr2

        for i in range(2, len(nums)): #start from 3rd eleemnt
            if arr1[-1] > arr2[-1]: #last element of arr1 is greater than last of arr2
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1+arr2