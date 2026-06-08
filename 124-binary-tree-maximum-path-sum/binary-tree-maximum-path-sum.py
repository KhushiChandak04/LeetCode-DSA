# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = float('-inf') #initialise sum
        def dfs(node): #recursive fnc
            if not node:
                return 0 #base condition
            left = max(0, dfs(node.left)) #eliminates -ves
            right = max(0, dfs(node.right))
            
            self.ans = max(self.ans, left+right+node.val) #pass thru current node
            return node.val + max(left, right) #return to one side parent
        dfs(root) #run dfs fnc for root node
        return self.ans