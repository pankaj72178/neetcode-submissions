class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        t = max(piles)

        if(n==h):
            return t

        def ispossible(k):
            hours = 0

            for pile in piles:
                if( pile%k > 0):
                    hours = hours + pile//k + 1
                else:
                    hours += pile//k

            return hours <= h
        
        low = 1
        high = t

        while low<high:

            mid = low + (high-low)//2

            if(ispossible(mid)):
                high = mid
            else:
                low = mid+1
        return low