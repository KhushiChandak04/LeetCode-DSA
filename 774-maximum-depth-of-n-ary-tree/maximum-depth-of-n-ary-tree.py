"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        
        depth = 0

        for child in root.children:
            depth = max(depth, self.maxDepth(child))

        return depth + 1 #as depth cannot be 0, min has to be 1