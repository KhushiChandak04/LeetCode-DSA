class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = [[] for i in range(n)] #create adj list

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u) #add connections in both the directions

        visited = [False]*n
        stack=[source]

        #perform dfs
        while stack:
            node = stack.pop() #removes the last vertex, which makes this DFS

            if node == destination:
                return True #destination reached

            if visited[node]:
                continue
            
            visited[node] = True #set the node to visited

            for nei in graph[node]: #chk all neighbours, and visit them
                if not visited[nei]:
                    stack.append(nei)
        return False