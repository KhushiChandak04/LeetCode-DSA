# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        #preorder - root -> left -> right... first element in this list is root of entire tree
        #inorder - left -> root -> right
        if not preorder:
            return None #empty tree
        
        root_value = preorder[0] #first element of preorder is root
        root = TreeNode(root_value)
        root_index = inorder.index(root_value) #find out where root is present in inorder

        #left subtree - nodes before root are left subtree inorder sequence
        left_inorder = inorder[:root_index] #slice array
        left_size = len(left_inorder) #no.of nodes in left subtree
        left_preorder = preorder[1: 1 + left_size] #skip first element and take size + 1

        #right subtree - nodes after root belong to right subtree inorder sequence
        right_inorder = inorder[root_index + 1:]
        right_preorder = preorder[1+ left_size:]

        #build subtrees now after defining them
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root