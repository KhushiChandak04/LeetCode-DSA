# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2): #reusing 2 list merge wala solution
        dummy = ListNode(0)
        current = dummy
        while list1 and list2: #till they are not null
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2
        return dummy.next

    def mergeKLists(self, lists): #define a recursive fnc for k lists
        merged = None #initially nothing merged
        for k in lists: #k sorted lists
            merged = self.mergeTwoLists(merged, k) #use 2 wla fnc here call it
        return merged