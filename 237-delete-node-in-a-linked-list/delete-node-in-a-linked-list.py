# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
#trick question as here we are not given prev node, cuz generally to delete a node in LL we do prev.next = node.next, but here we copy next node kaval into prev node and skip the next wala node here 
        node.val = node.next.val #copy next node's val
        node.next = node.next.next #skip next node