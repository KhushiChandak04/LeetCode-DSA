# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root: #until while traversal root is reached
            if p.val < root.val and q.val < root.val:
                root = root.left #lcs on left side
            elif p.val > root.val and q.val > root.val:
                root = root.right #lcs on right side 
            else:
                return root