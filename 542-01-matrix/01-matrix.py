class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        queue = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    mat[i][j] = float('inf')
                else:
                    queue.append([i,j,0])

        # bfs 
        while queue: 
            curr_x, curr_y, dist = queue.pop(0)

            if mat[curr_x][curr_y] > dist:
                mat[curr_x][curr_y] = dist
            
            for x,y in dirs:
                next_x = curr_x + x
                next_y = curr_y + y


                if next_x < 0 or next_x > len(mat)-1 or next_y < 0 or next_y > len(mat[0])-1:
                    continue
        
                if mat[next_x][next_y] == float('inf'):
                    queue.append([next_x, next_y, dist + 1])


        return mat






        

        