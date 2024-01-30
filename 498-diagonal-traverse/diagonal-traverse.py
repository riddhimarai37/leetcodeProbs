# examples:         
# [[1,2,3],
# [4,5,6],
# [7,8,9]]



class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        res = []

        curr_row, curr_col = 0,0

        going_up = True

        while len(res) != rows*cols:
            if going_up:
                while curr_row >= 0 and curr_col < cols:
                    res.append(mat[curr_row][curr_col])
                    curr_row -= 1
                    curr_col += 1
                # go back to last element within bounds
                if curr_col == cols:
                    curr_col -= 1 
                    curr_row += 2
                else:
                    curr_row +=1 

                going_up = False
            else:
                while curr_row < rows and curr_col >= 0:
                    res.append(mat[curr_row][curr_col])
                    curr_row += 1
                    curr_col -= 1
                # go back to last element within bounds
                if curr_row == rows:
                    curr_row -= 1
                    curr_col += 2
                else:
                    curr_col += 1

                going_up = True

        return res






        # if len(mat) == 1:
        #     return mat[0]
    
        # visited = set()

        # def create_diagonal(i,j):
        #     if (i,j) in visited:
        #         return []

        #     visited.add((i,j))
        #     new_diag = [mat[i][j]]
        #     row = i+1
        #     col = j-1

        #     while row < len(mat) and col >= 0:
        #         visited.add((row,col))
        #         new_diag.append(mat[row][col])
        #         row += 1
        #         col -=1 

        #     return new_diag

        # res = []

        # for i in range(len(mat)):
        #     for j in range(len(mat[i])):
        #         if (i,j) in visited:
        #             continue
        #         else:
        #             diagonal = create_diagonal(i,j)
        #             for d in diagonal:
        #                 res.append(d)

        # return res




            



