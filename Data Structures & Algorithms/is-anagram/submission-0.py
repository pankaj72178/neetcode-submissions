class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s1 = [0]*26
        t1 = [0]*26

        n = len(s)
        m = len(t)

        if m!=n:
            return False

        for i in range(n):
            s1[ord(s[i])-97]+=1
            t1[ord(t[i])-97]+=1
        
        for i in range(26):
            if(s1[i]!=t1[i]):
                return False
        return True