class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        ans = [] #stores the bulbs remaining

        for bulb in bulbs:
            if bulb in ans:
                ans.remove(bulb)
            else:
                ans.append(bulb)
                
        #sort in asc order
        ans.sort()
        return ans