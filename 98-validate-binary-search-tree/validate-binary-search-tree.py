# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node, low, high):
            if not node:
                return True #valid bst
            #node must lie in a range
            if node.val <= low or node.val >= high:
                return False
            return (
                dfs(node.left, low, node.val) and
                dfs (node.right, node.val, high)
            )
        return dfs(root, float('-inf'), float('inf'))
        #lies b/w this range