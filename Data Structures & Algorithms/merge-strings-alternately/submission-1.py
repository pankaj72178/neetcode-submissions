class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ""
        n1 = len(word1)
        n2 = len(word2)

        i = 0
        while (i<max(n1,n2)):
            if(i<n1):
                word3 = word3 + word1[i]
            if(i<n2):
                word3 = word3 + word2[i]
            i+=1
            
        return word3