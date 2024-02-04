class Solution:
    # have a visited list with visited indices
    # iterate through the matrix and continue going down a diagonal until we either see a nonequal value or we're outof bounds 
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) == 1 or len(matrix[0]) == 1:
            return True

        visited = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (i,j) in visited:
                    continue

                val = matrix[i][j]
                visited.append((i,j))

                # check diagonals
                row = i+1
                col = j+1
                while row < len(matrix) and col < len(matrix[i]):
                    if (row,col) not in visited:
                        if matrix[row][col] != val:
                            return False
                        visited.append((row,col))
                    row += 1
                    col += 1

        return True 


                
                        



        