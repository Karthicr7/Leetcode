class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        a=abs(30*hour - 5.5*minutes)
        if a>180:
            a=abs(360-a)
        return a
        