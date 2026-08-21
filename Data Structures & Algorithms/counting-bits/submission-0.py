class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = [0]*(n+1)

        for i in range(1,n+1):
            t = i
            k = 0
            while t>0:
                k = k + t%2
                t = t//2
            ans[i] = k
        return ans