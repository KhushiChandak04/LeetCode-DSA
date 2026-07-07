# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #inorder: left -> root -> right
        answer = [] #stores ans nodes
        
        def inorder(node): # bfs fnc here
            if node is None:
                return
            inorder(node.left) #visit left subtree
            answer.append(node.val) #visit current node
            inorder(node.right) #visit right subtree
            
        inorder(root)
        return answer