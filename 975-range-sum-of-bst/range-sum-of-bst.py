# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def traverse(node, low, high):
            if not node:
                return 0

            if node.val >= low and node.val <= high:
                return node.val + traverse(node.left, low, high) + traverse(node.right, low, high)
            elif node.val < low:
                return traverse(node.right, low, high)
            else:
                return traverse(node.left, low, high)

        return traverse(root, low, high)






        
















        # if not root:
        #     return 0

        # if root.val >= low and root.val <= high:
        #     return root.val + self.rangeSumBST(root.left,low, high) + self.rangeSumBST(root.right,low,high)
        # elif root.val < low:
        #     return self.rangeSumBST(root.right, low, high) 
        # else:
        #     return self.rangeSumBST(root.left, low, high)

        
    # TIME O(N) Space O(N) b/c of the call stack
        