# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next: #if onli 1 node exists
            return None
        count = 0
        curr = head #initialise ptr

        while curr: #till curr reaches the end of LL
            count += 1 #visited nodes
            curr = curr.next
        middle = count // 2
        curr = head

        for i in range(middle - 1): #w ehave to delete the node before it as counting begins from 0
            curr = curr.next
        curr.next = curr.next.next
        return head