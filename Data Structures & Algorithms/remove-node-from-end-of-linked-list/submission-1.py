# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0

        while curr:
            size += 1
            curr = curr.next
        
        if(size == n):
            return head.next

        temp = head
        for i in range(size-n-1):
            temp = temp.next
        
        temp.next = temp.next.next

        return head