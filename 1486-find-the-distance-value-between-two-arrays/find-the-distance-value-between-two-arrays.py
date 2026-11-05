class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0
        for num in arr1:
            found = False

            # compare it with every element in arr2
            for x in arr2:
                if abs(num - x) <= d:
                    found = True
                    break

            # count only if no close element was found
            if found == False:
                count += 1

        return count