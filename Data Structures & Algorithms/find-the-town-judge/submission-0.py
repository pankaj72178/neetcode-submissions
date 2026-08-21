class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        s = set()
        t = 0

        m = len(trust)
        judge = 1

        for i in range(m):
            s.add(trust[i][0])

        for i in range(1,n+1):
            if(i not in s):
                judge = i
                break
        
        for i in range(m):
            if(trust[i][1]==judge):
                t+=1
        if(t==n-1):
            return judge
        return -1