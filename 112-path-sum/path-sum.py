# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False #empty tree
        
        if root.left is None and root.right is None: #check if leaf node
            return root.val == targetSum #this will gimme a bool result
        
        rem = targetSum - root.val #subtract current node value, chk left and right subtrees

        return (
            self.hasPathSum(root.left, rem) or self.hasPathSum(root.right, rem)
        )