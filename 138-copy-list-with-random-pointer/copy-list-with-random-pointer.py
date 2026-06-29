"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None #blank LL case
        hashmap = {} #dictionary to store original -> copied node
        curr = head #initilise position

        while curr: #till end of LL, make copies
            hashmap[curr] = Node(curr.val) #stores curr val in blank hashmap, with same val
            curr = curr.next #traverse ahead
        
        #now next task is to cinnect and link those copied nodes
        curr = head
        while curr:
            copy = hashmap[curr] #get copied version of current node
            if curr.next:
                copy.next = hashmap[curr.next] #connect next ptr
            if curr.random:
                copy.random = hashmap[curr.random] #connect random ptr
            curr = curr.next

        return hashmap[head] #returns copied LL