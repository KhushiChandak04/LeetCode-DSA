# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #fast moves twice as fast as slow, so when fast reaches end, slow is the middle
        fast = head
        slow = head #initial ptrs

        while fast and fast.next: #till end
            slow = slow.next
            fast = fast.next.next
        return slow