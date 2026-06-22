# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0) #fake node before head
        dummy.next = head
        group_prev = dummy #node before current k grp

        while True:
            kth = group_prev #last node of current grp
            for _ in range(k):
                kth = kth.next #move ahead till k is reached
                if not kth:
                    return dummy.next
            group_next = kth.next #save next grp ka start
            #reverse current grp
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next #save next node
                curr.next = prev #reverse ptr
                prev = curr #move prev ahead
                curr = temp #move curr forward

            temp = group_prev.next #old grp becomes new tail
            group_prev.next = kth
            group_prev = temp 
