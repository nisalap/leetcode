class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        c = len(matrix)
        r = len(matrix[0])
        col = [[0 for i in range(c)] for j in range(r)]
        for i in range(c):
            for j in range(r):
                col[j][i] = matrix[i][j]
        return col
