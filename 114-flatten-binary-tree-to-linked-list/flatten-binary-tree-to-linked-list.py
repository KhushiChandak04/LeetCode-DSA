# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return #if tree is empty

        nodes = [] #stores node in preorder

        def preorder(node):
            
            #nodes = []
            if node is None:
                return
            nodes.append(node) #append current node thats thr root

            #preorder -- root -> left -> right
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        #now connect the nodes like linked list
        for i in range(len(nodes) -1):

            #left pointer should be empty and right should point to next node
            nodes[i].left = None
            nodes[i].right = nodes[i+1]
        
        #last nodes have no next
        nodes[-1].left = None
        nodes[-1].right = None