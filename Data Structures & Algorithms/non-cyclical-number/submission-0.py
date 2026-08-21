class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        def changeNumber(num):
            
            sm = 0
            while num:
                rem = num%10
                sm = sm + rem**2
                num = num//10
            return sm
        
        while True:
            if n in s:
                return False

            if (n == 1):
                return True
            
            s.add(n)
            n = changeNumber(n)