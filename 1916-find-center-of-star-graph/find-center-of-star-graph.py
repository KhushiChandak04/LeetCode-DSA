class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        #center is the node that connects to every node
        first_edge = edges[0]
        second_edge = edges[1]

        if first_edge[0] == second_edge[0] or first_edge[0] == second_edge[1]: #check whc node is common
            return first_edge[0]

        return first_edge[1]