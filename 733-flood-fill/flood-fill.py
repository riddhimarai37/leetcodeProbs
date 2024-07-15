class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        prev_color = image[sr][sc]

        if prev_color == color:
            return image
        
        def dfs(x, y):
            if image[x][y] == prev_color:
                image[x][y] = color

                if x-1 >= 0:
                    dfs(x-1,y)
                if x+1 < r:
                    dfs(x+1,y)
                if y-1 >= 0:
                    dfs(x,y-1)
                if y+1 < c:
                    dfs(x, y+1)

        dfs(sr,sc)
        return image

















        
        # r = len(image)
        # c = len(image[0])
        # init_color = image[sr][sc]
        # if init_color == color:
        #     return image

        # def dfs(x, y):
        #     if image[x][y] == init_color:
        #         image[x][y] = color
        #         if x >= 1:
        #             dfs(x-1, y)
        #         if x + 1 < r:
        #             dfs(x+1, y)
        #         if y >= 1:
        #             dfs(x, y-1)
        #         if y + 1 < c:
        #             dfs(x, y+1)
            
            

        # dfs(sr, sc)
        # return image

        # Time: O(N)
        # Space: O(N)

        

        