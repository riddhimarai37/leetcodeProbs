# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        p1 = head
        p2 = head.next

        while p2 and p2.next:
            if p1 == p2:
                return True
            
            p1 = p1.next
            p2 = p2.next.next
            
        return False

        

















        # if not head or not head.next: 
        #     return False

        # slow = fast = head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True

        # return False



















        # slow = head
        # fast = head

        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast == slow:
        #         return True
        # return False




        # # if not head:
        # #     return False

        # # left = head
        # # right = head.next

        # # while left != right:
        # #     if not right or not right.next:
        # #         return False
        # #     left = left.next
        # #     right = right.next.next

        # # return True
        
     

