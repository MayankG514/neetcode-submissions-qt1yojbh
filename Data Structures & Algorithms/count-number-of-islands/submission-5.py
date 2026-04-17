class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        R, C = len(grid), len(grid[0])
        

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (0<=nr<R and 0<=nc<C and grid[nr][nc]=="1" and (nr,nc) not in visit):
                        q.append((nr,nc))
                        bfs(nr,nc)
        
        islands = 0
        for i in range(R):
            for j in range(C):
                if (i,j) not in visit and grid[i][j]=="1":
                    bfs(i,j)
                    islands+=1
        return islands
        