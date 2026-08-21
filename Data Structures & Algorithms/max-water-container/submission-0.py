class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l,r = 0,n-1
        res = 0
        curr = 0

        while l<r:
            lmax,rmax = heights[l],heights[r]
            curr = (r-l)*(min(lmax,rmax))
            res = max(curr,res)
            if(lmax<rmax):
                l+=1
            else:
                r-=1
        return res