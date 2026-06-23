# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        #step 1 - find if cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: #cycle found here
            #find the cycle ka start then, that will be head
                ptr1 = head
                ptr2 = slow
                while ptr1 != ptr2:
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next #traverse ahead
                return ptr1 #start of cycle
        return None #no cycle