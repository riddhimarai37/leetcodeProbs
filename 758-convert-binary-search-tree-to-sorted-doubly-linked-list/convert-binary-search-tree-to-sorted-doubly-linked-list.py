"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# have a head node
# start a dfs on root: process in order of left --> root --> right 

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        self.first = None
        self.last = None

        self.inorder_link(root)

        # make list circular 
        self.first.left = self.last
        self.last.right = self.first

        return self.first

    def inorder_link(self, node):
        if node:
            self.inorder_link(node.left)
        
            if not self.last:
                self.first = node
            else:
                node.left = self.last
                self.last.right = node

            self.last = node

            self.inorder_link(node.right)


    # time: O(N) 
    # Space: inorder: O(1)


        

        

        