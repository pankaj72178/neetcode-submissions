class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        lmin = [0]*n
        rmax = [0]*n
        lmin[0],rmax[-1] = prices[0],prices[-1]
        for i in range(1,n):
            if(lmin[i-1]>prices[i]):
                lmin[i] = prices[i]
            else:
                lmin[i] = lmin[i-1]
        for i in range(n-2,-1,-1):
            if(rmax[i+1]<prices[i]):
                rmax[i] = prices[i]
            else:
                rmax[i] = rmax[i+1]
        res = 0
        for i in range(n):
            res = max(res,rmax[i]-lmin[i])
        return res