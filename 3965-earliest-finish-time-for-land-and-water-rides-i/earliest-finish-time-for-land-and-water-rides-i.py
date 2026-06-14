class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        ans = float('inf') #initialise to max for minimum time
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
            
            #land -> water is one approach
                landFinish = landStartTime[i] + landDuration[i]
                waterStart = max(landFinish, waterStartTime[j])
                ans = min(ans, waterStart + waterDuration[j])
            #water -> land is another approach
                waterFinish = waterStartTime[j] + waterDuration[j]
                landStart = max(waterFinish, landStartTime[i])
                ans = min(ans, landStart + landDuration[i])
        return ans