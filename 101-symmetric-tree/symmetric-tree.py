# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = []
        stack.append([root.left, root.right])

        while stack:
            left,right = stack.pop()

            if left and right:
                if left.val != right.val:
                    return False

                stack.append([left.left,right.right])
                stack.append([left.right, right.left])

            elif left or right:
                return False

        return True

        



        
















        # recursive solution
        # if not root: return True

        # def recurse(left, right):
        #     if not left and not right:
        #         return True

        #     if not left or not right:
        #         return False

        #     if left.val != right.val:
        #         return False

        #     return recurse(left.left, right.right) and recurse(left.right, right.left)

        # return recurse(root.left,root.right)
            


        