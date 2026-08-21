class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []

        dict = {"2" : "abc", "3" : "def", "4" : "ghi", 
                "5" : "jkl", "6" : "mno", "7" : "pqrs", 
                "8" : "tuv", "9" : "wxyz"}

        if(len(digits)==0):
            return []

        def combination(i,s):

            if(i==len(digits)):
                ans.append("".join(s))
                return
            
            tmp = dict.get(digits[i])

            for j in range(len(tmp)):
                ch = tmp[j]
                s.append(ch)
                combination(i+1, s)
                s.pop()
        
        combination(0,[])

        return ans