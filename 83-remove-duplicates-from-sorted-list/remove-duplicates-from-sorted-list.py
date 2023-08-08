# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head 
        if head.next == None:
            return head

        prev = curr = head

        while curr:
            # edge case where inital head is a duplicate
            while curr and prev.val == curr.val:
                curr = curr.next
            prev.next = curr

            prev = curr

        return head

