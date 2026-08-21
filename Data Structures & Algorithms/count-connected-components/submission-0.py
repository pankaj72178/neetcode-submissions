class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        d = {i:[] for i in range(n)}
        visited = set()
        ans = 0

        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)

            for j in d[i]:
                dfs(j)
        
        for i in range(n):
            if i not in visited:
                ans += 1
                dfs(i)
        return ans