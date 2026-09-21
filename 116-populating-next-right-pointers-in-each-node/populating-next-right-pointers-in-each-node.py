"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        
        #connect left child to right child
        if root.left:
            root.left.next = root.right
        
        #connect right child to next parents left child
        if root.right and root.next:
            root.right.next = root.next.left
        
        #do the same recursively for right and left subtrees
        self.connect(root.left)
        self.connect(root.right)

        return root