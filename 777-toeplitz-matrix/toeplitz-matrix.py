class Solution:
    # optimal solution: compare every value to it's top-left neighbor: if not equal return false
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # check if current point is part of a diagonal
                if i > 0 and j > 0 and matrix[i][j] != matrix[i-1][j-1]:
                    return False

        return True
             