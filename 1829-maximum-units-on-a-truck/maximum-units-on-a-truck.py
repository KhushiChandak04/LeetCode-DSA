class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        #sort box type in descending order, as more units contaainer will come first
        #truck size is no. of boxes it can take up
        boxTypes.sort(key = lambda x:x[1], reverse = True)
        total_units = 0

        for boxes, units in boxTypes:
            if boxes <= truckSize:
        # Take all boxes of this type
                total_units += boxes * units
                truckSize -= boxes
            else:
        # Truck cannot fit all boxes, so take only remaining capacity
                total_units += truckSize * units
                truckSize = 0
        return total_units