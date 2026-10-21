# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #core idea is that we will save the vals of nodes in an array, then sort that array and then place them in LL

        if head is None:
            return None #if list is empty

        values = [] #stores node vals
        curr = head #start point

        while curr:
            values.append(curr.val)
            curr = curr.next #move the ptr ahead
        values.sort()

        curr = head #put sorted val in LL back, create a head
        i = 0

        while curr:
            curr.val = values[i]
            curr = curr.next
            i += 1
        return head