# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Initialize dummy node, previous node, current node
        prev = dummy = ListNode(val=0, next=head)
        curr = head

        # Iterate through LL (while the current node is not null)
        while curr:
            # while current node is val, set current node to next
            while curr and curr.val == val:
                curr = curr.next
            # if current node is not equal then set prev.next to curr.
            prev.next = curr

            # if curr exist, move prev to current node and current node to next and repeat
            if curr:
                prev = prev.next
                curr = curr.next
        # Return dummy.next
        return dummy.next