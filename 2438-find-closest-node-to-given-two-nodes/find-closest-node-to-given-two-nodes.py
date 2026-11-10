class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        def findDist(start): #create a function to find distance frm start node
            dist = [-1] * len(edges)
            steps = 0
            node = start

            #follow till the edges repeat or path ends
            while node != -1 and dist[node] == -1:
                dist[node] = steps
                steps += 1
                node = edges[node]

            return dist
        
        dist1 = findDist(node1) #find their distances from starting node
        dist2 = findDist(node2)

        ans = -1
        smallest = float('inf') #start with the largest val possible

        #chk every node here
        for i in range(len(edges)):

            if dist1[i] != -1 and dist2[i] != -1: #is reachable or no
                maximum = max(dist1[i], dist2[i])

                if maximum < smallest:
                    smallest = maximum
                    ans = i
        return ans