# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res = []

        # def traverse(level, node):
        #     if not node:
        #         return None

        #     if level > len(res)-1:
        #         res.append([node.val])
        #     else:
        #         res[level].append(node.val)

        #     traverse(level + 1, node.left)
        #     traverse(level + 1, node.right)

        # traverse(0,root)

        # return res

        #Time: O(n) Space: O(n)





    # dequeue approach 

        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res