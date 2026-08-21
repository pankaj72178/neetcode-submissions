class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(start, temp):

            if len(temp) == k:
                ans.append(temp[:])
                return

            for i in range(start, n + 1):
                temp.append(i)
                backtrack(i + 1, temp)
                temp.pop()
        
        backtrack(1,[])
        return ans