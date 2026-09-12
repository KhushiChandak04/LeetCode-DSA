# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        #preorder = root -> left -> right

        if len(preorder) == 0:
            return None #if there are no elements

        root = TreeNode(preorder[0]) #root is the first element in preorder
        i = 1 #values greater than root
        while i < len(preorder) and preorder[i] < root.val:
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i]) #smaller values go to the left as it is bst
        root.right = self.bstFromPreorder(preorder[i:]) #larger values go to the right
        return root