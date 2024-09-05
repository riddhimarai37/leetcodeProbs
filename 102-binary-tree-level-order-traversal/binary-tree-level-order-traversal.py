# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def traverse(level, node):
            if not node:
                return None

            if level > len(res)-1:
                res.append([node.val])
            else:
                res[level].append(node.val)

            traverse(level + 1, node.left)
            traverse(level + 1, node.right)

        traverse(0,root)

        return res