"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# class Solution:
#     def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         # recursive solution

#         if not root:
#             return root

#         # current and temp node 
#         head = temp = Node()

#         def helper(node):
#             nonlocal head
#             if not node:
#                 return 
            
#             # traverse through left subtree
#             helper(node.left)
#             # perform linking on current node
#             head.right = node
#             node.left = head
#             head = node
#             # traverse through right subtree
#             helper(node.right)

#         helper(root)
        
#         # complete circularity 
#         temp.right.left = head
#         head.right = temp.right

#         return temp.right


    # time: O(N) 
    # Space: inorder: O(N) bc recursive stack




class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #Iterate solution using a stack
        if not root:
            return None

        stack = [root]
        first = None
        curr = root.left
        last = None

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
                continue
            if stack:
                curr = stack.pop()
                if not first:
                    first = curr
                if last:
                    last.right = curr
                    curr.left = last
                last = curr
                curr = curr.right 

        first.left = last
        last.right = first

        return first



        

        