class Solution:
    def solve(self, board: List[List[str]]) -> None:

        row = len(board)
        col = len(board[0])

        visited = [[0]*col for i in range(row)]

        def dfs(i,j):

            if(i>0 and board[i-1][j]=='O' and visited[i-1][j]==0):
                visited[i-1][j] = 1
                dfs(i-1,j)

            if(j>0 and board[i][j-1]=='O' and visited[i][j-1]==0):
                visited[i][j-1] = 1
                dfs(i,j-1)

            if(i+1<row and board[i+1][j]=='O' and visited[i+1][j]==0):
                visited[i+1][j] = 1
                dfs(i+1,j)

            if(j+1<col and board[i][j+1]=='O' and visited[i][j+1]==0):
                visited[i][j+1] = 1
                dfs(i,j+1)
            
            return
        
        for i in range(row):
            for j in range(col):
                if(i==0 or i==row-1 or j==0 or j==col-1):
                    if(board[i][j]=='O' and visited[i][j]==0):
                        visited[i][j] = 1
                        dfs(i,j)

        for i in range(row):
            for j in range(col):

                if(visited[i][j]==1):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"