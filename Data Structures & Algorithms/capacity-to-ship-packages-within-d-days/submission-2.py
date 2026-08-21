class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canship(cap):
            d = 1
            cur = 0

            for w in weights:
                if(cur+w>cap):
                    d+=1
                    cur = 0
                cur += w
                
            return d<=days

        low = max(weights)
        high = sum(weights)

        while low<high:

            mid = low + (high-low)//2

            if(canship(mid)):
                high = mid
            else:
                low = mid+1
        return high