# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.min_diff = float('inf')
        self.min_diff_value = -1


        def traverse(node):
            if not node:
                return 0

            curr_diff = abs(target - node.val)

            if curr_diff < self.min_diff:
                self.min_diff = curr_diff
                self.min_diff_value = node.val
            elif curr_diff == self.min_diff:
                self.min_diff_value = min(node.val, self.min_diff_value)
                
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.min_diff_value
        