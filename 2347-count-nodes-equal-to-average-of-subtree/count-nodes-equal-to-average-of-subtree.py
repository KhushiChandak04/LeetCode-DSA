# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #core idea use dfs
        self.answer = 0 #initilise

        def dfs(node):
            if node is None:
                return 0,0 #there is no node, its count and sum both are 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            average = total_sum // total_count

            if node.val == average: #check if any node is equal to avg of the subtree
                self.answer += 1

            return total_sum, total_count

        dfs(root)
        return self.answer