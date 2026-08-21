class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s)-1
        k = 0
        while low<high:
            if(not s[low].isalnum()):
                low+=1
            elif(not s[high].isalnum()):
                high-=1
            else:
                if(s[low].lower()!=s[high].lower()):
                    k = 1
                else:
                    low+=1
                    high-=1
            if(k==1):
                return False
        return True