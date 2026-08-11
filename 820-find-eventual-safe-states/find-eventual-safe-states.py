class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        #terminal node -> no outgoing edges, safe node -> where path leads to a terminal node or another safe node, return all safe nodes in asc order

        #0 = unvisited, 1 = cuurently visiting/ or if traversed again, cycle found, 2 = visited/safe
        n = len(graph)
        state = [0] * n #initilise graph

        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True

            state[node] = 1 #for current visit

            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            state[node] = 2 #after its visited
            return True
        
        return [i for i in range(n) if dfs(i)]