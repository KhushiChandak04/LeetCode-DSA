class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        target = len(graph)-1

        #find all paths possib;e
        def dfs(node):
            path.append(node)

            #chk if destination reached
            if node == target:
                ans.append(path[:]) #save copy of current path
            
            else:
                for nei in graph[node]: #chk all neighbours
                    dfs(nei)
            
            path.pop() #backtracking, remove curr node, so that dfs can explore other path

        dfs(0) #start frm 0
        return ans