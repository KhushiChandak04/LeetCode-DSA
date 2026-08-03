class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maximum = max(candies) #find current max of candies
        result = [] #multiple ans possible

        for candy in candies:
            if candy + extraCandies >= maximum:
                result.append(True) #boolean
            else:
                result.append(False)
        return result