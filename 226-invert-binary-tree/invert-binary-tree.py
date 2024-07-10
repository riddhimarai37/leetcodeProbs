# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(node):
            if not node: 
                return None
            
            node.left, node.right = node.right, node.left

            invert(node.left)
            invert(node.right)

        invert(root)
        return root















        
        # if not root:
        #     return root
        # # swap the children
        # root.left, root.right = root.right, root.left

        # # perform recursive operation
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

        # Time: O(N), Space: O(N) - Call Stack
        