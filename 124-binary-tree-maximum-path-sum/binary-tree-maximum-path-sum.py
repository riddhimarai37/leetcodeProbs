# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        # return max path sum WITHOUT SPLITTING
        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            # compute max path sum WITH A SPLIT AT ROOT 
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # return value will be max value we get WITHOUT SPLITTING
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]



        

        