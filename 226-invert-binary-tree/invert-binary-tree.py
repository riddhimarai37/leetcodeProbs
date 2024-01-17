# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root
        elif not root.left:
            root.left = self.invertTree(root.right)
            root.right = None
            return root
        elif not root.right:
            root.right = self.invertTree(root.left)
            root.left = None
            return root 

        left = root.left
        right = root.right
        
        root.left = right
        root.right = left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root







        