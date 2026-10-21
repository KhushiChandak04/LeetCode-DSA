class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #use prims algo here, but o(n2) complexity

        n = len(points)
        visited = [0]*n

        #min cost to connect all pts
        dist = [float('inf')]*n #set to highest
        dist[0] = 0 #base case, start frm 0

        ans = 0 

        for _ in range(n):
            node = -1 #find the nearest unconnected node
            for i in range(n):
                if not visited[i]:
                    if node == -1 or dist[i] < dist[node]: #choose pt with smallest cost
                        node = i
            visited[node] = True #mark node as visited

            ans += dist[node]

            for i in range(n): #chk all rem pts
                if not visited[i]:
                #we find manhattan dist
                    cost = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])

                #update if this cost is less
                    if cost < dist[i]:
                        dist[i] = cost
        return ans