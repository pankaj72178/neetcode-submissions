class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        tree = {i:[] for i in range(n)}


        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
            
        visited = set()

        def dfs(node, parent):

            if node in visited:
                return False

            visited.add(node)

            for nei in tree[node]:
                if nei == parent:
                    continue

                if not dfs(nei, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n