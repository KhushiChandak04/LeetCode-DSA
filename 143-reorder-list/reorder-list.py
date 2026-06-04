# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        if not head: #if empty LL case
            return
        nodes = [] #creates empty array to store nodes
        current = head #initialise to start from here
        while current:
            nodes.append(current)
            current = current.next #access all nodes
        left = 0
        right = len(nodes) - 1 #initialise pts
        while left < right:
            nodes[left].next = nodes[right] #ptr connection build
            left += 1
            if left > right:
                break
            nodes[right].next = nodes[left]
            right -= 1 #do till there is no next node
        nodes[left].next = None