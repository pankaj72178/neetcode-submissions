class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        lmax = [0]*(n)
        rmax = [0]*(n)
        lmax[0] = height[0]
        rmax[-1] = height[-1]
        for i in range(1,n):
            if(height[i]>lmax[i-1]):
                lmax[i] = height[i]
            else:
                lmax[i] = lmax[i-1]
    
        for i in range(n-2,-1,-1):
            if(height[i]>rmax[i+1]):
                rmax[i] = height[i]
            else:
                rmax[i] = rmax[i+1]

        for i in range(n):
            res = res + min(lmax[i],rmax[i]) - height[i]
        
        return res