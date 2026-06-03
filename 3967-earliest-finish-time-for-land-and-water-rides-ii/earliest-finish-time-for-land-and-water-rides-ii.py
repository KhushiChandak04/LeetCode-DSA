from bisect import bisect_right

class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):

        ans = float('inf')
        water = sorted(zip(waterStartTime, waterDuration))
        ws = [x[0] for x in water] #due totimed out issue
        m = len(water)
        prefix = [0] * m
        prefix[0] = water[0][1]

        for i in range(1, m):
            prefix[i] = min(prefix[i-1], water[i][1])

        #minimum (start+duration) from i onwards
        suffix = [0] * m
        suffix[-1] = water[-1][0] + water[-1][1]

        for i in range(m-2, -1, -1):
            suffix[i] = min(
                suffix[i+1],
                water[i][0] + water[i][1]
            )
        #land -> water approach
        for i in range(len(landStartTime)):
            landFinish = landStartTime[i] + landDuration[i]
            pos = bisect_right(ws, landFinish)
            #water already opened
            if pos > 0:
                ans = min(
                    ans,
                    landFinish + prefix[pos-1]
                )
            #water opens later
            if pos < m:
                ans = min(
                    ans,
                    suffix[pos]
                )

        land = sorted(zip(landStartTime, landDuration))

        ls = [x[0] for x in land]

        n = len(land)

        prefix = [0] * n
        prefix[0] = land[0][1]

        for i in range(1, n):
            prefix[i] = min(prefix[i-1], land[i][1])

        suffix = [0] * n
        suffix[-1] = land[-1][0] + land[-1][1]

        for i in range(n-2, -1, -1):
            suffix[i] = min(
                suffix[i+1],
                land[i][0] + land[i][1]
            )

        #water -> land
        for j in range(len(waterStartTime)):
            waterFinish = waterStartTime[j] + waterDuration[j]
            pos = bisect_right(ls, waterFinish)
            #land already opened
            if pos > 0:
                ans = min(
                    ans,
                    waterFinish + prefix[pos-1]
                )
            #land opens later
            if pos < n:
                ans = min(
                    ans,
                    suffix[pos]
                )
        return ans