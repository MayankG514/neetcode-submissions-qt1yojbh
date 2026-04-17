class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        R,C = len(grid), len(grid[0])
        
        def bfs(r,c):
            q = collections.deque()
            grid[r][c]=0
            q.append((r,c))
            islandArea = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (0<=nr<R and 0<=nc<C and grid[nr][nc]==1):
                        islandArea+=1
                        grid[nr][nc]=0
                        q.append((nr,nc))
            return islandArea
            
                
        maxL = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    l = bfs(r,c)
                    maxL = max(maxL,l)
        return maxL