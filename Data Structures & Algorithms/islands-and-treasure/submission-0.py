class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        q = collections.deque()
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        INF = 2**31 - 1
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if (0<=nr<R and 0<=nc<C and grid[nr][nc] == INF):
                    grid[nr][nc] = 1+grid[row][col]
                    q.append((nr,nc))
        
    

        
