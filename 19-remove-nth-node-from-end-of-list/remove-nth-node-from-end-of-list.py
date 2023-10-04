# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        curr = head
        while curr:
            length += 1
            curr = curr.next

        remove_idx = length - n
        if length == 1:
            return head.next
        elif remove_idx == 0:
            return head.next

        prev = curr = head

        curr_idx = 0
        while curr:
            if curr_idx == remove_idx:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
            curr_idx += 1

            
        return head