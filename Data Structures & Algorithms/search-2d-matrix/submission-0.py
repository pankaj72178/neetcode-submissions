class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        i,j = 0,m-1


        while i<n and j>=0:
            res = matrix[i][j]
            if(res==target):
                return True
            elif(res>target):
                j-=1
            else:
                i+=1
        return False