# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy #initialise ptrs slow and fast at 0th
        fast = dummy
        for i in range (n): #we maintain a gap of n b/w the 2 ptrs
            fast = fast.next #for traversal
        while fast.next: #until null has reached
            slow = slow.next #traverse both ptrs
            fast = fast.next
        slow.next = slow.next.next #deletes and skips nth from end imp step
        return dummy.next