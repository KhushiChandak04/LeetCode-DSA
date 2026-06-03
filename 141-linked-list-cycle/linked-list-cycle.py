# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head #initialise 2 ptrs which are fast and slow traversing
        fast = head
        while fast and fast.next: #they are not null traverse till end
            slow = slow.next
            fast = fast.next.next
            if slow == fast: #loop exists as fast catches slow
                return True
        return False