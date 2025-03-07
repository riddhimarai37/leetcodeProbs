# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iteratively 
        prev = None
        curr = dummy = head

        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
        
        return prev
            
            
            

            

            

            





            
            


 
            

             




        














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