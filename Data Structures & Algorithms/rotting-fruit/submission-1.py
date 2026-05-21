class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        time = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        fresh = 0
        q = collections.deque()

        for r in range(R):
            for c in range(C):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh+=1

        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (0<=nr<R and 0<=nc<C and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1