class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = []

        board = [['.' for _ in range(n)] for _ in range(n)]

        def isvalid(i, j):

            for row in range(i):
                if board[row][j] == 'Q':
                    return False

            row, col = i, j
            while row > 0 and col > 0:
                row -= 1
                col -= 1
                if board[row][col] == 'Q':
                    return False

            row, col = i, j
            while row > 0 and col < n - 1:
                row -= 1
                col += 1
                if board[row][col] == 'Q':
                    return False

            return True

        def generate(row):

            if row == n:
                ans.append([''.join(r) for r in board])
                return

            for col in range(n):

                if isvalid(row, col):

                    board[row][col] = 'Q'

                    generate(row + 1)

                    board[row][col] = '.'

        generate(0)

        return ans