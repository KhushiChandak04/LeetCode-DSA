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
            take = min(boxes, truckSize) #no of boxes we can actually take
            total_units += take * units
            truckSize -= take

            #if truckSize == 0: #till truck is filled fully
                #break
        return total_units