class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        low = 0
        high = n-1

        while low < high:
            matrix[low], matrix[high] = matrix[high], matrix[low]
            low += 1
            high -= 1

        for i in range(n):
            for j in range(0,i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]