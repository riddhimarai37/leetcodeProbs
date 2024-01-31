# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        
        if not root:
            return []

        rows = []
        queue = deque([(0,root)])

        while queue:
            row, node = queue.popleft()
            if len(rows) <= row:
                rows.append([node.val])
            else:
                rows[row].append(node.val)

            if node.left: 
                queue.append((row + 1, node.left))
            if node.right:
                queue.append((row+1, node.right))

        res = []
        for curr in rows:
            # add right most value to res
            res.append(curr[-1])

        return res
