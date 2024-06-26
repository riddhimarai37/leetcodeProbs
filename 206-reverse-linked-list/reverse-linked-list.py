# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp
        
        return prev

            

             




        















        # if head == None or head.next == None:
        #     return head

        # prev = None
        # curr = head

        # while curr:
        #     # next value to look at
        #     next = curr.next

        #     # reversing 
        #     curr.next = prev 
        #     prev = curr
        #     curr = next
        # return prev


        # explanation
        # Initialize a previous node, a current node.
        # prev, curr = None, head

        # # While current node is not null
        # while curr:
        #     # Initialize a next node to temporarily hold the next node
        #     next = curr.next
        #     # Point current node .next to previous node
        #     curr.next = prev
        #     # Set prev node to current node
        #     prev = curr
        #     # Set current node to next node
        #     curr = next
        
        # # Return previous node
        # return prev
        # if not head or not head.next:
        #     return head

        # prev = None
        # curr = head

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp

        # return prev

