# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Initialize a front pointer
        self.frontPointer = head

        # Define Recursive Call: To check front pointer against entire stack of nodes(reversed nodes).
        def recursiveCheck(curr: Optional[ListNode]) -> bool:
            if curr:
                # Recursive check on next node otherwise return false
                if not recursiveCheck(curr.next):
                    return False
                # Ensure front pointer is equal to stack node otherwise return false
                elif self.frontPointer.val != curr.val:
                    return False
                # Move front pointer
                else:
                    self.frontPointer = self.frontPointer.next
            # At end of call stack return True
            return True
            
        # Return Recursive Call
        return recursiveCheck(head)
            