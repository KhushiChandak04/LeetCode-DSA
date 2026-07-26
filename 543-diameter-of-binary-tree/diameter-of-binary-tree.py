# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #core idea - diameter = height of left subtree + height of right subtree
        #use DFS approach
        self.diameter = 0 #initilise
        def height(node):
            if not node:
                return 0 #edge case, height of 0 tree is 0 and not none
            left = height(node.left)
            right = height(node.right)

            #update the maximum diameter
            self.diameter = max(self.diameter, left+right)
            return 1 + max(right, left)
        height(root)
        return self.diameter