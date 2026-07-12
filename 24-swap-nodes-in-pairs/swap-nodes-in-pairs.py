# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy #initilise ptr position

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next #2 ptrs here are 1st and 2nd
            #swap
            first.next = second.next #disconnect 1st from 2nd
            second.next = first #put 2nd pointing to 1st
            prev.next = second #connect prev node to 2nd
            prev = first #move prev to end ptr

        return dummy.next