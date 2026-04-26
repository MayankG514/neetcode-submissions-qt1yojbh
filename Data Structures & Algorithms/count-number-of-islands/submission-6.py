class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        islands = 0
        R,C = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]


        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr,nc = row+dr, col+dc
                    if (0<=nr<R and 0<=nc<C and (nr,nc) not in visit and grid[nr][nc]=="1"):
                        q.append((nr,nc))
                        bfs(nr,nc)
            


        for r in range(R):
            for c in range(C):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1

        return islands
                
