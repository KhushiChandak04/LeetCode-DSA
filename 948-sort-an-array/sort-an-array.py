class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            result = []
            i, j = 0,0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            while i < len(left): #if the elements are remaining
                result.append(left[i])
                i += 1
            while j < len(right):
                result.append(right[j])
                j += 1
            
            return result
        return mergeSort(nums)