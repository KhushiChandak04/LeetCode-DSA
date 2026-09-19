class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        #horizontal distance of circle frm rect
        if xCenter < x1:
            dx = x1 - xCenter
        elif xCenter > x2:
            dx = xCenter - x2
        else:
            dx = 0

        #vertical distance of circle frm rect
        if yCenter < y1:
            dy = y1 - yCenter
        elif yCenter > y2:
            dy = yCenter - y2
        else:
            dy = 0

        #check distance from circle to rectangle
        return dx*dx + dy*dy <= radius * radius