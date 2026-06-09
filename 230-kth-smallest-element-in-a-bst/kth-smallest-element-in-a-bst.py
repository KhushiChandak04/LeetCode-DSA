# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        nums = []
        def inorder(node): #inorder is left > root > right
            if not node:
                return
            inorder(node.left) #visit left subtree first
            nums.append(node.val) #store current node after visinting left subtree
            inorder(node.right) #visit right subtree last
        inorder(root)
        return nums[k-1]