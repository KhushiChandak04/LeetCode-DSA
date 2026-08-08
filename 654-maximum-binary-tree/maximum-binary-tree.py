# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None #no numbers, no tree
        maximum = max(nums)
        #find index of maximum in the array of nums
        index = nums.index(maximum)
        root = TreeNode(maximum) #create a tree node

        #everything to the left of index becomes left subtree
        root.left = self.constructMaximumBinaryTree(nums[:index])
        #everything to the right of index becomes right subtree
        root.right = self.constructMaximumBinaryTree(nums[index + 1:])

        return root