class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        #use graph colouring pattern here, bfs search
        colour = [-1] * len(graph)
        #-1  = not coloured yet, 0 = first grp, 1 = sencond grp

        for start in range(len(graph)):

            #if node is alrd coloured then sjkip it
            if colour[start] != -1:
                continue
            colour[start] = 0 #give current start node as 0
            queue = [start] #put starting node into the queue

            while queue:
                node = queue.pop(0) #take the first node

                for neighbour in graph[node]: #check every neighbour
                    #make 0 as 1 and 1 as 0 to every neighbour
                    if colour[neighbour] == -1:

                        colour[neighbour] = 1-colour[node]
                        queue.append(neighbour)

                    elif colour[neighbour] == colour[node]: #neighbour has same colour as the node thenreturn False
                        return False

        return True #otherwise