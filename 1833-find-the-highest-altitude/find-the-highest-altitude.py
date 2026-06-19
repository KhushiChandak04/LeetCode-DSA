class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = 0 #initilise current
        highest = 0 #maximum altitude seen so far

        for i in gain:
            altitude += i
            highest = max(highest, altitude)
        return highest