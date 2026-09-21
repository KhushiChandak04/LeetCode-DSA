# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        seen = set()
        
        def dfs(node):

            if node is None:
                return False #empty tree

            needed = k - node.val
            if needed in seen:
                return True
            seen.add(node.val) #store current value here

            #search left and right here
            if dfs(node.left):
                return True
            if dfs(node.right):
                return True
            else:
                return False
                
        return dfs(root)