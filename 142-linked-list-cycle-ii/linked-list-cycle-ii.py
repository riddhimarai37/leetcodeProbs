# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        pos = -1
        cycle_exists = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle_exists = True
                break

        if not cycle_exists:
            return None

        e = slow
        h = head
        while e.next:
            if e == h:
                return e
            e = e.next
            h = h.next

            
        