# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None #empty LL

        curr = head #start from the first node
        while curr.next:
            if curr.val == curr.next.val: #have same velue as it is sorted
                curr.next = curr.next.next #skip that node
            else:
                curr = curr.next #move ahead
        return head