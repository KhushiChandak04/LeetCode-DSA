# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        if root is None:
            return 0 #empty tree

        def countPaths(node, total): #count paths from current node

            if node is None: #empty case
                return 0

            total -= node.val #sub node val frm total
            count = 0

            if total == 0:
                count += 1 #we found a path
            
            count += countPaths(node.left, total) #chk left and right childers
            count += countPaths(node.right, total)

            return count

        return (countPaths(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum))