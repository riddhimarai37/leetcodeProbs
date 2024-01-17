# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive solution 
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# dfs solution 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root,1]]
        res = 0

        while stack:
            node,depth = stack.pop()
            if node: 
                res = max(depth, res)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res






        