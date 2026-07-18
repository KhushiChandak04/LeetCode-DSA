class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = min(nums)
        largest = max(nums)

        while smallest != 0: #use euclidian algo
            largest, smallest = smallest, largest % smallest
            
        return largest