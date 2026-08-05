# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        #core idea - in BST, elements left to root are less than root and those on right are greater than root
        if not root:
            return None
        if root.val == val:
            return root #return the entire subtree
        if val < root.val:
            return self.searchBST(root.left, val) #search left subtree
        else:
            return self.searchBST(root.right, val) #search right subtree