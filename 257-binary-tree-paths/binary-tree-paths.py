# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        answer = []
        current = []
        
        def dfs(node):
            if node == None:
                return #node does not exist

            current.append(str(node.val)) #convert the node value to string
            if node.left == None and node.right == None: #it is a leaf node
                path = "" #convert path into a req string
                for i in range(len(current)):
                    path += current[i]
                    if i != len(current) - 1:
                        path += "->" #add arrow till last node
                answer.append(path)
            else:
                dfs(node.left) #visit left subtree
                dfs(node.right) #visit right subtree
            current.pop() #backtrack

        dfs(root)
        return answer