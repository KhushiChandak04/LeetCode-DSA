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
        if root is None:
            return None
        
        #if we found p or q:
        if root == p or root == q:
            return root
        
        #search in left and right subtree
        left = self.lowestCommonAncestor(root.left, p,q)
        right = self.lowestCommonAncestor(root.right, p, q)

        #if one node is on left and other is on right , current node is lca
        if left and right:
            return root #final condition here
        
        #onli one left node or onli one right node
        if left:
            return left
        else:
            return right