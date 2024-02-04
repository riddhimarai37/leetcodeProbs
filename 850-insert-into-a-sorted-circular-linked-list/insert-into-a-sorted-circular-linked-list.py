# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next
# """
# # keep track of prev and curr node 
# # insertVal is the largest value --> keep going throuhg the list until we find left val < right 
# # insertVal is th smallest value --> keep going until we find left val < right 

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node()
            node.val = insertVal
            node.next = node
            return node

        prev = head
        cur = head.next

        while prev.next != head:
            # add value in the middle of LL
            if insertVal >= prev.val and insertVal <= cur.val:
                break
            # insert at beginning or end of LL
            elif prev.val > cur.val and (insertVal > prev.val or insertVal < cur.val):
                break
            prev = prev.next
            cur = cur.next
                
        node = Node(insertVal, cur)
        prev.next = node
        return head
