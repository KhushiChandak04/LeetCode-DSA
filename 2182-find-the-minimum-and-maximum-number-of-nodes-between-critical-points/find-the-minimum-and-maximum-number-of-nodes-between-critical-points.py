# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        prev = head #initilise LL ptrs for traversal
        curr = head.next

        first_critical = -1
        last_critical = -1
        min_distance = float('inf')
        index = 1

        while curr.next: #till last node of LL
            next_node = curr.next
            if ((curr.val > prev.val and curr.val > next_node.val) or (curr.val < prev.val and curr.val < next_node.val)): #critical pt condition
                if first_critical == -1:
                    first_critical = index
                else:
                    min_distance = min(min_distance, index - last_critical)
                last_critical = index

            prev = curr
            curr = curr.next #move all ptrs ahead
            index += 1

        if first_critical == -1 or first_critical == last_critical:
            return [-1,-1]

        max_distance = last_critical - first_critical
        return[min_distance, max_distance]