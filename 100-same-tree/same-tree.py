# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q: #empty nodes
            return True
        if not p or not q: #either node not exists
            return False
        if p.val != q.val: #if both nodes exists but their values do not match
            return False
        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )