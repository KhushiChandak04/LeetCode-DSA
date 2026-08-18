class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {} #store how many sub arrays stores nos 
        for i in range(len(nums) - k + 1): #subarrays of size k
            subarray = nums[i:i+k] #take subarray starting from i
            for num in set(subarray):
                if num not in count:
                    count[num] = 0
                count[num] += 1

        answer = -1 #default return value
        for num in count:
            if count[num] == 1:
                answer = max(answer, num)
        return answer