from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify grid in-place instead.
        """

        INF = 2147483647

        row = len(grid)
        col = len(grid[0])

        q = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i, j))

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while q:
            i, j = q.popleft()

            for dr, dc in directions:
                nr = i + dr
                nc = j + dc

                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[i][j] + 1
                    q.append((nr, nc))