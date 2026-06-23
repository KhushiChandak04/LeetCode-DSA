"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head #empty LL
        self.dfs(head)
        return head

    def dfs(self, node):
        curr = node
        last = None
        while curr:
            next_node = curr.next
            #if curr node has child
            if curr.child:
                child_head = curr.child
                #flatten child list
                child_tail = self.dfs(child_head)

                #connect curr -> child
                curr.next = child_head
                child_head.prev = curr

                #connect child tail -> original next
                if next_node: #traverse till end
                    child_tail.next = next_node
                    next_node.prev =  child_tail
                curr.child = None
                last = child_tail
            else:
                last = curr
            curr = next_node
        return last