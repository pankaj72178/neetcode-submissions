class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        arr = []

        # Convert first linked list to array
        if len(lists) == 0:
            return None

        for node in lists:
            current = node

            while current:
                arr.append(current.val)
                current = current.next

        # Sort all values
        arr.sort()

        # Create result linked list
        dummy = ListNode(0)
        current = dummy

        for value in arr:
            current.next = ListNode(value)
            current = current.next

        return dummy.next