# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        nodes = {} #create a blank list to store all nodes
        children = set() #stores all child values
        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent) #create a parent node if not present
            if child not in nodes:
                nodes[child] = TreeNode(child) #create child if not present
            #make the connections 
            if isLeft == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            children.add(child) #adds into children set
            
        #find root - a node that has never been a child
        for parent, child, isLeft in descriptions:
            if parent not in children: #check for parent node in children list
                return nodes[parent]