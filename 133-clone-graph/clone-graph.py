"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        cloned = {} #original node: copied node hashmap

        def dfs(node): #fnc for traversal
            if node in cloned:
                return cloned[node]
            newNode = Node(node.val) #creates a copy of node here
            cloned[node] = newNode

            for neighbour in node.neighbors:
                newNode.neighbors.append(dfs(neighbour)) #clones neighbours of graph
            return newNode
        return dfs(node)