class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        mxprft = 0
        for i in range(len(prices)):
            mn = min(mn,prices[i])
            mxprft = max(mxprft,prices[i]-mn)
        return mxprft