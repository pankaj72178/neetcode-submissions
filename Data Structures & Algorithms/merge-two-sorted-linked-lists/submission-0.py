# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode(0)
        tail = dummy

        curr1 = list1
        curr2 = list2

        while curr1 and curr2:

            if curr1.val <= curr2.val:
                tail.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                tail.next = ListNode(curr2.val)
                curr2 = curr2.next

            tail = tail.next

        while curr1:
            tail.next = ListNode(curr1.val)
            tail = tail.next
            curr1 = curr1.next

        while curr2:
            tail.next = ListNode(curr2.val)
            tail = tail.next
            curr2 = curr2.next

        return dummy.next