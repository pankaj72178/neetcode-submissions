class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mnp = prices[0]
        prft = 0
        for i in range(1,n):
            if (prices[i]<=mnp):
                mnp = prices[i]
            elif (prices[i]>mnp):
                prft = prft+prices[i]-mnp
                mnp = prices[i]
        return prft