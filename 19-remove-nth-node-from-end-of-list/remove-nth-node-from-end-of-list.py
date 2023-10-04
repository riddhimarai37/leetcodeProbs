# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # CODEPATH SOLUTION

        temp = ListNode(val = 0, next = head)

        first = temp
        second = temp

        # Advances first pointer so that the gap between first and second is n nodes apart
        for i in range (n+1):
            first = first.next

        # While the first pointer does not equal null move both first and second to maintain the gap and get nth node from the end
        while (first != None):
            first = first.next 
            second = second.next

        # Delte the node being pointed to by second
        second.next = second.next.next

        return temp.next



        # MY SOLUTION 
        # length = 0

        # curr = head
        # while curr:
        #     length += 1
        #     curr = curr.next

        # remove_idx = length - n
        # if length == 1:
        #     return head.next
        # elif remove_idx == 0:
        #     return head.next

        # prev = curr = head

        # curr_idx = 0
        # while curr:
        #     if curr_idx == remove_idx:
        #         prev.next = curr.next
        #         curr = curr.next
        #     else:
        #         prev = curr
        #         curr = curr.next
        #     curr_idx += 1

        # return head