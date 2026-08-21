class Solution:
    def reverse(self, x: int) -> int:
        
        modp = (1<<31) - 1
        modn = -1*(1<<31)
        neg = False

        if(x<0):
            neg = True
        
        x = abs(x)

        ans = 0

        while x:
            rem = x%10
            ans = ans*10 + rem
            x = x//10
        
        if(neg):
            ans = (-1)*ans
        if(ans>modp or ans<modn):
            return 0
        return ans
