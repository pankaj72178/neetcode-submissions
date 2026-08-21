class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def isPalindrome(sub_str):
            
            l = 0
            r = len(sub_str) - 1
        
            while l<r:
                if(sub_str[l] != sub_str[r]):
                    return False
                l += 1
                r -= 1
            
            return True
        
        n = len(s)
        res = 0

        for i in range(n):
            for j in range(i,n):
                if(isPalindrome(s[i:j+1])):
                    res += 1
            
        return res