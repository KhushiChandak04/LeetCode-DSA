# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0) #helps build ans list
        curr = dummy
        carry = 0 #initilise

        while l1 or l2 or carry: #continue until any list has nodes or till carry lasts
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 #continue till list lasts, else use 0
            #add digits
            total = val1 + val2 + carry
            #digit to store in current node 
            digit = total % 10
            carry = total // 10
            #create new node -----> to store ans
            curr.next = ListNode(digit)
            curr = curr.next #traverse ahead

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy.next