# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None #initialise fresh ptrs
        current = head
        while current: #till it is not null i.e traverses till end of LL
            front = current.next #shows now connection of LL
            current.next = prev
            prev = current #for traversal
            current = front
        return prev        