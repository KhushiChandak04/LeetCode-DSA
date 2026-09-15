# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #the question asks for the maximum-sum subtree that IS a BST..so you need to look for a smaller subtree inside the given tree that satisfies BST rules

        self.answer = 0

        def dfs(node): #return format is BST(true/false), min val, max val, sum
            if node is None:
                return True, float('inf'), float('-inf'), 0
            
            #get info from right and left subtree
            leftBST, leftMin, leftMax, leftSum = dfs(node.left)
            rightBST, rightMin, rightMax, rightSum = dfs(node.right)

            #check if selected tree is a bst
            if leftBST and rightBST and leftMax < node.val < rightMin:
                #calculate sum
                total = leftSum + rightSum + node.val
                self.answer = max(self.answer, total) #save the maximum sum

                #return info about BST
                return True, min(leftMin, node.val), max(rightMax, node.val), total
            
            #not a bst case
            return False, 0, 0, 0
        dfs(root)
        return self.answer