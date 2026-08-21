class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if (obstacleGrid[-1][-1] == 1):
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if (m==1):
            for i in range(n):
                if obstacleGrid[0][i] == 1:
                    return 0
        
        if (n == 1):
            for j in range(m):
                if obstacleGrid[j][0] == 1:
                    return 0
        
        if (m == 1 or n == 1):
            return 1
        
        mat = [[0]*n for i in range(m)]

        for i in range(n-2,-1,-1):
            k = 0
            if (obstacleGrid[-1][i] == 1):
                k = 1
                while i >= 0:
                    mat[-1][i] = 0
                    i -= 1
            if (k==1):
                break
            mat[-1][i] = 1
        
        for j in range(m-2,-1,-1):
            k = 0
            if (obstacleGrid[j][-1] == 1):
                k = 1
                while j >= 0:
                    mat[j][-1] = 0
                    j -= 1
            if (k==1):
                break
            mat[j][-1] = 1

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if (obstacleGrid[i][j] == 1):
                    mat[i][j] = 0
                else:
                    mat[i][j] = mat[i+1][j] + mat[i][j+1]
        
        return mat[0][0]