class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        

        def dfs(crs):         
            if crs in visit:
                return False
            
            if preMap[crs] == []:
                return True

            visit.add(crs)
            for p in preMap[crs]:
                if not dfs(p):
                    return False
            
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True


