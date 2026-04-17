class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adjList = [[] for _ in range(n)]

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(i):
            if adjList[i] == [] or i in visit:
                return
            
            visit.add(i)
            
            for j in range(len(adjList[i])):
                dfs(adjList[i][j])     
            
            
        
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count+=1
        
        return count
