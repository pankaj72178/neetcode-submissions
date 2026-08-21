class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        visited = [[0]*col for i in range(row)]
        ans = 0

        def island(i,j,row,col):

            area = 1

            if(i>0 and grid[i-1][j]==1 and visited[i-1][j]==0):
                visited[i-1][j] = 1
                area += island(i-1,j,row,col)

            if(j>0 and grid[i][j-1]==1 and visited[i][j-1]==0):
                visited[i][j-1] = 1
                area += island(i,j-1,row,col)
            
            if(i+1<row and grid[i+1][j]==1 and visited[i+1][j]==0):
                visited[i+1][j] = 1
                area += island(i+1,j,row,col)

            if(j+1<col and grid[i][j+1]==1 and visited[i][j+1]==0):
                visited[i][j+1] = 1
                area += island(i,j+1,row,col)
            
            return area
        
        for i in range(row):
            for j in range(col):
                if(grid[i][j]==1 and visited[i][j]==0):
                    visited[i][j] = 1
                    val = island(i,j,row,col)
                    ans = max(ans,val)
        
        return ans