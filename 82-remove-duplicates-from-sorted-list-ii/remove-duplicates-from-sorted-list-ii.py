# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_count = {}

        curr = head

        while curr:
            if curr.val not in num_count:
                num_count[curr.val] = 1
            else:
                num_count[curr.val] += 1

            curr = curr.next

        temp = result = ListNode()

        for curr_num in num_count:
            if num_count[curr_num] == 1:
                result.next = ListNode(curr_num)
                result = result.next

        return temp.next
        