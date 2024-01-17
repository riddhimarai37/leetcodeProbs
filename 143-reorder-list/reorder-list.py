# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the mid point
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        # splitting the lists
        slow.next = None

        # reverse second half of the list
        prev = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

        # merge two halves together
        second = prev # second is currently set to null bc of reversing; set it to prev 
        first = head

        while first and second:
            # going to be breaking the links
            temp1 = first.next 
            temp2 = second.next

            first.next = second
            second.next = temp1 # interweaving in between first and first.next

            # shifting our pointers
            first = temp1
            second = temp2
            
            
    




