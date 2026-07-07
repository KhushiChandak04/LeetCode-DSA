# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        answer = []

        def dfs(node, depth): #depth = current level
            if not node:
                return
        #if we are visiting the node for the first time, it has to be the right most node
            if depth == len(answer):
                answer.append(node.val)

            #visit right subtree first
            dfs(node.right, depth + 1)
            #then visit left subtree
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return answer