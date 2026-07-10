# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0 #bfs approach
            
        queue = deque() #double ended queue stores (node, index)
        queue.append((root, 0))

        max_width = 0
        while queue:
            level_size = len(queue)
            
            #index of 1st node at this level 
            first = queue[0][1]
            #index of last node at this level
            last = queue[-1][1]

            width = last - first + 1 #width of current level
            max_width = max(max_width, width)

            for i in range(level_size):
                node, index = queue.popleft()
                #left child
                if node.left:
                    queue.append((node.left, 2 * index + 1))
                #right child
                if node.right:
                    queue.append((node.right, 2 * index + 2))
        return max_width