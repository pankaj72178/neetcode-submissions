# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        temp = l3

        carry = 0

        while l1 and l2:
            sm = carry + l1.val + l2.val
            carry = sm//10
            l1 = l1.next 
            l2 = l2.next
            temp.next = ListNode(sm%10)
            temp = temp.next
        
        while l1:
            sm = carry + l1.val
            carry = sm//10
            l1 = l1.next
            temp.next = ListNode(sm%10)
            temp = temp.next
        
        while l2:
            sm = carry + l2.val
            carry = sm//10
            l2 = l2.next
            temp.next = ListNode(sm%10)
            temp = temp.next
        
        if carry>0:
            temp.next = ListNode(carry%10)
            # temp = temp.next
            # carry = carry//10
        
        return l3.next
