class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        column = len(grid[0])

        ans = 0

        for i in range(row):
            for j in range(column):

                if(grid[i][j]==1):
                    ans+=4

                    if(j>0 and grid[i][j-1]==1):
                        ans-=1
                    
                    if(i>0 and grid[i-1][j]==1):
                        ans-=1
                    
                    if(j+1<column and grid[i][j+1]==1):
                        ans-=1
                    
                    if(i+1<row and grid[i+1][j]==1):
                        ans-=1
        return ans
                    
                    