class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        h1, m1, s1 = startTime.split(":") #split the start time
        start = int(h1) * 3600 + int(m1) * 60 + int(s1) #convert to seconds

        h2, m2, s2 = endTime.split(":") #split end time
        end = int(h2) * 3600 + int(m2) * 60 + int(s2) #again convert this to seconds, in the same unit
        return end - start