"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # recursive solution

        if not root:
            return root

        # current and temp node 
        head = temp = Node()

        def helper(node):
            nonlocal head
            if not node:
                return 
            
            # traverse through left subtree
            helper(node.left)
            # perform linking on current node
            head.right = node
            node.left = head
            head = node
            # traverse through right subtree
            helper(node.right)

        helper(root)
        
        temp.right.left = head
        head.right = temp.right

        return temp.right


        















    #     if not root:
    #         return None

    #     self.first = None
    #     self.last = None

    #     self.inorder_link(root)

    #     # make list circular 
    #     self.first.left = self.last
    #     self.last.right = self.first

    #     return self.first

    # def inorder_link(self, node):
    #     if node:
    #         self.inorder_link(node.left)
        
    #         if not self.last:
    #             self.first = node
    #         else:
    #             node.left = self.last
    #             self.last.right = node

    #         self.last = node

    #         self.inorder_link(node.right)


    # time: O(N) 
    # Space: inorder: O(N) bc recursive stack


        

        

        