# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        def dfs(node, row):
            if not node:
                return 

            if len(res) - 1 < row:
                res.append(node.val)

            dfs(node.right, row + 1)
            dfs(node.left, row + 1)

            return res

        return dfs(root, 0)
            
























        # from collections import deque
        
        # if not root:
        #     return []

        # rows = []
        # queue = deque([(0,root)])

        # while queue:
        #     row, node = queue.popleft()
        #     if len(rows) <= row:
        #         rows.append([node.val])
        #     else:
        #         rows[row].append(node.val)

        #     if node.left: 
        #         queue.append((row + 1, node.left))
        #     if node.right:
        #         queue.append((row+1, node.right))

        # res = []
        # for curr in rows:
        #     # add right most value to res
        #     res.append(curr[-1])

        # return res


# neetcode solution 
# class Solution:
#     def rightSideView(self, root: TreeNode) -> List[int]:
#         res = []
#         q = collections.deque([root])

#         while q:
#             rightSide = None
#             qLen = len(q)

#             for i in range(qLen):
#                 node = q.popleft()
#                 if node:
#                     rightSide = node
#                     q.append(node.left)
#                     q.append(node.right)
#             if rightSide:
#                 res.append(rightSide.val)
#         return res



