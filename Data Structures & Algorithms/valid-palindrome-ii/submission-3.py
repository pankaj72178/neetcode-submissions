class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispal(low,high):
            while low<high:
                if(s[low]!=s[high]):
                    return False
                high-=1
                low+=1
            return True
        
        low = 0
        high = len(s)-1

        while low<high:
            if(s[low]!=s[high]):
                return ispal(low+1,high) or ispal(low,high-1)
            low+=1
            high-=1
        return True