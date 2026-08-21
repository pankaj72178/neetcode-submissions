class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ""
        n1 = len(word1)
        n2 = len(word2)

        i = 0
        j = 0
        while (i<n1 and j<n2):
            word3 = word3 + word1[i]
            word3 = word3 + word2[j]
            i+=1
            j+=1
        while (i<n1):
            word3 = word3 + word1[i]
            i+=1
        while (j<n2):
            word3 = word3 + word2[j]
            j+=1
        return word3
        
        