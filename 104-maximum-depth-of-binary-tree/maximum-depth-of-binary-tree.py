# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, level):
            if not node:
                return 0

            left = dfs(node.left, level + 1)
            right = dfs(node.right, level + 1)

            return 1 + max(left, right)

        return dfs(root, 0)



    