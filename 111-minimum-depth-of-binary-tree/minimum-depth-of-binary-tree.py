# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: #blank tree
            return 0
        if not root.left and not root.right: #leaf node with no children
            return 1
        if not root.left: #onli right child exists
            return 1+ self.minDepth(root.right)
        if not root.right: #onli left child exists
            return 1+ self.minDepth(root.left)
        #if both childen exists
        return 1 + min(self.minDepth(root.right), self.minDepth(root.left))