# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def depth(node):
            if not node:
                return 0

            left_length = depth(node.left)
            right_length = depth(node.right)

            diameter = left_length + right_length

            self.max_diameter = max(self.max_diameter, diameter)
            return 1 + max(left_length, right_length)

        depth(root)
        return self.max_diameter