# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def dfs(node):
            if not node:
                return [True, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            bal = left[0] and right[0] and abs(right[1]-left[1]) <= 1

            return [bal, 1 + max(left[1], right[1])]


        return dfs(root)[0]











        # def dfs(root):
        #     if not root:
        #         return [True, 0]

        #     left = dfs(root.left) 
        #     right = dfs(root.right)

        #     bal = left[0] and right[0] and abs(right[1] - left[1]) <= 1

        #     return [bal, 1 + max(left[1], right[1])]

        # return dfs(root)[0]

        # Time: O(n) Space: O(n) bc of stack

            

        

            



        