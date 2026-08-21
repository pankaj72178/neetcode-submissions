class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        mat = [[0]*n for i in range(m)]
        mat[-1][-1] = grid[-1][-1]

        for i in range(n-2,-1,-1):
            mat[-1][i] = mat[-1][i+1] + grid[-1][i]
        
        for j in range(m-2,-1,-1):
            mat[j][-1] = mat[j+1][-1] + grid[j][-1]
        
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                mat[i][j] = min(mat[i][j+1], mat[i+1][j]) + grid[i][j]
        
        return mat[0][0]