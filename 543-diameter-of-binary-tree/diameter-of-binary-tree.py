# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max_length = 0
        def traverse(node):
            if not node:
                return 0

            left = traverse(node.left)
            right = traverse(node.right)
            diameter = left + right

            self.max_length = max(self.max_length, diameter)

            return 1 + max(left, right)

        traverse(root)
        return self.max_length

        




















        
        # self.max_diameter = 0
        # def depth(node):
        #     if not node:
        #         return 0

        #     left_length = depth(node.left)
        #     right_length = depth(node.right)

        #     diameter = left_length + right_length

        #     self.max_diameter = max(self.max_diameter, diameter)
        #     return 1 + max(left_length, right_length)

        # depth(root)
        # return self.max_diameter