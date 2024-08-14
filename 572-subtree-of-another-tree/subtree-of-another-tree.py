# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False

            if node1.val == node2.val:
                return same_tree(node1.left, node2.left) and same_tree(node1.right, node2.right)
            else:
                return False


        if not root and subRoot:
            return False
        if same_tree(root, subRoot):
            return True
        elif root.left or root.right:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return False


        