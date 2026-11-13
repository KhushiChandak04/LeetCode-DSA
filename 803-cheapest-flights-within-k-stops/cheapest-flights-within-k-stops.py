class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        #core logic, we use bellman ford here
        dist = [float('inf')] *n #store the minimum distance here
        dist[src] = 0 #initilise

        for i in range(k+1): #k stops, k+1 flights
            temp = dist[:] #make a copy of dist

            for u,v,price in flights:
                #u = start city, v= end city, price = flight cost

                if dist[u] != float('inf'): #chk if reachable
                    new_cost = dist[u] + price #calculate cost of reaching new city

                    if new_cost < temp[v]:
                        temp[v] = new_cost

            dist = temp #update dist arrar

        if dist[dst] == float('inf'): #chk if dist is reachable
            return -1
        return dist[dst]