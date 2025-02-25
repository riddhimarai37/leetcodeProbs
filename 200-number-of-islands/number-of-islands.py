class Solution:

        
    def numIslands(self, grid: List[List[str]]) -> int:
        def iterate(x,y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or (x,y) in island_set or grid[x][y] == '0':
                return 

            if grid[x][y] == '1':
                island_set.add((x,y))
                iterate(x+1, y)
                iterate(x-1,y)
                iterate(x,y+1)
                iterate(x,y-1)
                
        res = 0
        island_set = set()

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1' and (x,y) not in island_set:
                    res += 1
                    iterate(x,y)

        return res


                

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # if not grid or not grid[0]:
        #     return False

        # islands = 0
        # path = set()
        # rows = len(grid)
        # cols = len(grid[0])

        # def part_of_island(r,c):
        #     if (r < 0 or c < 0 or
        #         r >= rows or c >= cols or grid[r][c] == "0") or (r,c) in path:
        #         return 

        #     path.add((r,c))
        #     directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        #     for dr, dc in directions:
        #         part_of_island(r + dr, c + dc)

        
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r,c) not in path:
        #             islands += 1
        #             part_of_island(r,c)

        # return islands




            



        