# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        cols = defaultdict(list)
        queue = deque([(root, 0)])
        minCol = maxCol = 0
        
        while queue:
            node, col = queue.popleft()
            cols[col].append(node.val)

            minCol = min(col, minCol)
            maxCol = max(col, maxCol)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))


        res = []

        for c in range(minCol, maxCol + 1):
            res.append(cols[c])

        return res

       
       
        # if not root:
        #     return []

        # cols = defaultdict(list)
        # queue = deque([(root, 0)])  # (node, column)

        # while queue:
        #     node, col = queue.popleft()

        #     cols[col].append(node.val)

        #     if node.left:
        #         queue.append((node.left, col - 1))
        #     if node.right:
        #         queue.append((node.right, col + 1))

        # result = [cols[key] for key in range(min(cols), max(cols)+1)]
        # return result
            

        # # time O(N) space O(N)
            
