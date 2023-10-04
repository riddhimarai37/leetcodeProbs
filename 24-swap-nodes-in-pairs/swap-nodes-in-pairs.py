# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = temp = ListNode(val = 0, next = head)

        while prev.next and prev.next.next:
            # get the next node and next next node exist
            first = prev.next
            second = prev.next.next

            # set first.next to second.next, point to next node pair
            first.next = second.next
            # set sesocnd.next to first, perform the swap
            second.next = first
            # set prev.next to second, point to current node pair
            prev.next = second
            # set prev to first, set prev to node previous to next node pair
            prev = first

        return temp.next




        