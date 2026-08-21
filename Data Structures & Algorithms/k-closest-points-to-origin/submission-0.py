class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []

        for i in range(len(points)):
            arr.append([points[i][0]**2 + points[i][1]**2,i])
        
        arr.sort(key = lambda x:x[0])

        ans = []

        for i in range(k):
            ans.append(points[arr[i][1]])        
        return ans