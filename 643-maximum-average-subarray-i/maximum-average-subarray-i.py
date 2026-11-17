class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        total = 0 #claculate the sum of first k ele
        for i in range(k):
            total += nums[i]

        maximum = total #store total as maximum val

        for i in range(k,len(nums)): #move the window fwd
            total = total -nums[i-k] +nums[i] #add new element and remove the prev

            if total > maximum:
                maximum = total
        return maximum/float(k) #calcukate maximum avg