# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
#LL can only traverse ahead, it cannot move backwards, so thattswhy we need to reverse the 2nd half of LL and compare it
        slow = head #initilise slow and fast ptrs
        fast = head
        while fast and fast.next: #till the end of LL
            slow = slow.next
            fast = fast.next.next
        #reverse 2nd half of LL and chk to compare
        prev = None
        curr = slow #curr is middle as slow has reached the mid pt of LL
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #compare 1st half and 2nd half here
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True