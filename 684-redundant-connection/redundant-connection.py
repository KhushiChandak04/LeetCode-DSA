class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        parent = [i for i in range(n+1)] #each node is initially its own parent

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        for u,v in edges:
            root1 = find(u) #find grp of u
            root2 = find(v) #find grp of v

            if root1 == root2:
                return[u,v] #already connectd, so this edge creates a cycle

            parent[root1] = root2 #connect the 2 grps