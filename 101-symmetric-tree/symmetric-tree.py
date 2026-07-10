# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(left, right):
            if left == None and right == None:
                return True #both nodes are empty

            if left == None or right == None:
                return False #one exists and the other doesnot exist
            
            if left.val != right.val:
                return False #values do not match
        #check mirror
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        
        return dfs(root.left, root.right)