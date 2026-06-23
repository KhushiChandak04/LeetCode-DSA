# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        k = k % length #remove extra rotations

        for _ in range(k):
            curr = head #initilise ptr
            prev = None
            while curr.next: #traverse to last ptr
                prev = curr
                curr = curr.next
            #remove last node and move it to front
            prev.next = None
            curr.next = head
            head = curr
        return head