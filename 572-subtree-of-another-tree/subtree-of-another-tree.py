# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def isSame(p,q): #check for same subtree
            if not p and not q:
                return True #empty case
            if not p or not q: 
                return False #either of the subtree is not present
            if p.val != q.val:
                return False #values are not same
            return (
                isSame(p.left, q.left) and 
                isSame(p.right, q.right)
            )
        #dfs on root 
        def dfs(node):
            if not node:
                return False
            if isSame(node, subRoot):
                return True #check if root and subroot are same
            return(
                dfs(node.left) or 
                dfs(node.right)
            )
        return dfs(root)