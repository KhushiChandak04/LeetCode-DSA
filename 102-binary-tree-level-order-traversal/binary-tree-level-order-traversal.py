# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return[]
        result = [] #stores result
        q = deque([root]) #double ended queue = deque, tree traversal level by level we need queue
        while q: #till it reaches the end
            level = [] #stores a current level
            size = len(q)
            for i in range(size):
                node = q.popleft() #removes first node from the queue
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result