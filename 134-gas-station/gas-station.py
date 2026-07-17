class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        #if total gas is < total cost, impossible circuit
        if sum(gas) < sum(cost):
            return -1
        
        start = 0 #current start position
        tank = 0 #current gas capacity in tank

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            #if tank cant reach the station
            if tank < 0:
                start = i + 1 #fixate to a new start
                tank = 0 #restart the journey with empty tank
        return start