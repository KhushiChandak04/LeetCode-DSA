class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        #core idea - each node has almost 1 outgoing edge
        n = len(edges)
        visited = [False]* n #initilise dp arrray here
        ans = -1 #init

        for i in range(n):
            if visited[i]:
                continue
            curr = i #initilise curr ptr for traversal
            path = [] #list mutable
            pos = {} ##both mutable, key value pairs we need for dictionaries here

            while curr != -1 and not visited[curr]:
                visited[curr] = True #mark current node as visited 
                pos[curr] = len(path) #till the path continues
                path.append(curr)
                curr = edges[curr]

            if curr in pos:
                ans = max(ans, len(path)- pos[curr])
        
        return ans