# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #postorder: left -> right -> root
        answer = []
        def postorder(node):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            answer.append(node.val)
            
        postorder(root)
        return answer