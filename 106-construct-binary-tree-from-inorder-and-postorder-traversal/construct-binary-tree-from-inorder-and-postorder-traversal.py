# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int] #left > root > right
        :type postorder: List[int] #left > right > root
        :rtype: Optional[TreeNode]
        """
        indexMap ={} #create hash map for inorder
        for i in range (len(inorder)):
            indexMap[inorder[i]] = i #stores nodes in key value pair of order

        def build(left, right): #function for tree building
            if left > right: #base case epmty after all nodes removed
                return None
            rootVal = postorder.pop() #root is always the end for postorder
            root = TreeNode(rootVal) #creates node in ans tree
            mid = indexMap[rootVal] #find root position onli 1 main root

            #build right first since we are popping from end
            root.right = build(mid+1, right) #everything to right of mid is right subree
            root.left = build(left, mid-1) #everything to left of mid is left subtree
            return root
        return build(0, len(inorder) -1)