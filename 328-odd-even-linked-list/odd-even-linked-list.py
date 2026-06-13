# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next: #has 0 or 1 node so nothing to rearrange(base condn)
            return head
        odd = head #ptrs initialise
        even = head.next
        evenHead = even #saves the beginning of even list

        while even and even.next: #till we reach the end of list
            odd.next = even.next #connect the current odd node to next odd node
            odd = odd.next #move odd ptr ahead

            even.next = odd.next #connect the current even node to next even node
            even = even.next #move even ptr ahead

        odd.next = evenHead # link the even list after the odd ends
        return head