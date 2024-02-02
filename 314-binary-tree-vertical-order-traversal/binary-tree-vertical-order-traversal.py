# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# [3,9,20,null,null, 15, 7]
# return [[9], [3,15] , [20] , [7]]

# cols = {col_idx}
# res  = []
# dfs(node, curr_col, minCol, maxCol):
# if not node: return 
# cols[curr_col] = node.val
# dfs (node.left, curr_col - 1, minCol, maxCol)
# dfs (node.right, curr_col + 1, minCol, maxCol)
# dfs(root, 0, float(-inf), float(inf))
# go through the dictionary through the ranges of minCol and maxCol and append the values to results

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        cols = defaultdict(list)
        queue = deque([(root, 0)])  # (node, column)

        while queue:
            node, col = queue.popleft()

            cols[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        result = [cols[key] for key in range(min(cols), max(cols)+1)]
        return result
            

        # time O(N) space O(N)
            
