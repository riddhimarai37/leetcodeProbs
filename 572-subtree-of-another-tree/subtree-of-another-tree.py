# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def equalTree(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and root2 and root1.val == root2.val:
                return equalTree(root1.left, root2.left) and equalTree(root1.right, root2.right)
            else:
                return False


        if not root and not subRoot:
            return True
        if not root and subRoot: 
            return False
        if root and subRoot and root.val == subRoot.val:
            if equalTree(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        

        

        