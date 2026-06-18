class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        minute_angle = minutes * 6 #360/60 mins
        hour_angle = (hour % 12) * 30 + minutes * 0.5 #modulo as wrt 12.00 the angle we take
        diff = abs(hour_angle - minute_angle) #absolute value
        return min(diff, 360-diff) #minimum side angle