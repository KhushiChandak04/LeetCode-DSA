class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        #core idea - use dikjstras algo for shortest path in the graph
        graph = [[] for i in range(n+1)] #create the graph first

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        #core idea - use Dijkstra's algorithm for shortest path in the graph

        graph = [[] for i in range(n + 1)]  #create the graph first

        for u, v, w in times:
            graph[u].append((v, w))  #u = source, v = target, w = time taken

        dist = [float('inf')] * (n + 1)  #initialise distance of every node
        dist[k] = 0  #starting node has distance 0

        visited = [False] * (n + 1)  #keep track of visited nodes

        for i in range(n):
            node = -1  #find the closest node

            for j in range(1, n + 1):
                if not visited[j] and (node == -1 or dist[j] < dist[node]):
                    node = j  #choose the node with smallest distance

            if node == -1:
                break

            visited[node] = True  #mark node as visited

            for next_node, time in graph[node]:
                dist[next_node] = min(
                    dist[next_node],
                    dist[node] + time
                )  #update shortest distance

        ans = max(dist[1:])  #find the longest distance

        if ans == float('inf'):
            return -1  #node cannot be reached

        return ans