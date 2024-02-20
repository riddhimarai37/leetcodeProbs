class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = collections.deque([(0,0,1)]) # row col length
        visit = set((0,0)) 
        directions = [[0,1], [1,0], [0, -1], [-1,0],
                        [1,1], [-1,-1], [1,-1], [-1,1]]

        while queue:
            r,c,length = queue.popleft()
            # check if this is valid
            if r < 0 or c < 0 or r == N or c == N or grid[r][c] == 1:
                continue
            # check if we've reached the bottom right
            if r == N-1 and c == N-1:
                return length

            for dr, dc in directions:
                if (r+dr, c+dc) not in visit:
                    queue.append((r+dr, c+dc, length + 1))
                    visit.add((r+dr,c+dc))

        return -1
