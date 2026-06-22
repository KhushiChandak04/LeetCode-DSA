# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptr1 = headA #initilise 2 ptrs
        ptr2 = headB
        while ptr1 != ptr2:
            if ptr1:
                ptr1 = ptr1.next
            else:
                ptr1 = headB #ptr reaches end of list A, start traversing B
            if ptr2:
                ptr2 = ptr2.next
            else:
                ptr2 = headA #reaches the end of list B, start traversing A
        return ptr1