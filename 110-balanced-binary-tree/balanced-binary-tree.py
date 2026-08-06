# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        #core idea |height(left subtree) - height(right subtree)| <= 1
        def height(node):
            if not node:
                return 0 #empty tree

            #find height of left subtree
            left = height(node.left)
            if left == -1: #if left subtree is unbalanced
                return -1

            right = height(node.right) #same for height of right subtree
            if right == -1: #if right subtree is unbalanced
                return -1
            
            #if current node is unbalanced
            if abs(left-right) > 1:
                return -1
            return 1+max(left,right) #return currrent height 

        return height(root) != -1 #tree is balanced if height didnt return -1