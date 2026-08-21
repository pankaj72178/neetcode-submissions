class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {i:[] for i in range(numCourses)}

        for cr, pre in prerequisites:
            preMap[cr].append(pre)
        
        visited = set()


        def dfs(crs):
            if crs in visited:
                return False
            
            if preMap[crs] == []:
                return True
            
            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            preMap[crs] = []
            return True

        for cr in range(numCourses):
            if not dfs(cr):
                return False
        return True