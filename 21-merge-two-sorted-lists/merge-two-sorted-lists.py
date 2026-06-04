# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0) #initialise fake node
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val: #compare sorted nodes values
                current.next = list1
                list1 = list1.next #move ahead
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1: #if unequal and one of the lists ended
            current.next = list1
        else:
            current.next = list2
        return dummy.next #skips initial 0 node