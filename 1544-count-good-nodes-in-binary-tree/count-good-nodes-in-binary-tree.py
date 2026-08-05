# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # node is good if its value is greater than or equal to every value from the root to that node.
        def dfs(node, maxVal):
            if not node:
                return 0 #base case
            count = 0
            if node.val >= maxVal:
                count = 1
            #update maximum value seen so far
            maxVal = max(node.val, maxVal)

            #count good nodes on left and right subtrees seperately
            count += dfs(node.left, maxVal)
            count += dfs(node.right, maxVal)
            return count

        return dfs(root, root.val)