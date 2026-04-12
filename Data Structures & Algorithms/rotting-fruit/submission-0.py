class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        fresh =0
        q = collections.deque()
        time = 0
        direction = [[0,1],[0,-1],[-1,0],[1,0]]
        
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        
        while q and fresh > 0:
            
            for ind in range(len(q)):
                row,col = q.popleft()
                for dr, dc in direction:
                    nr, nc = row+dr, col +dc
                    if (0<=nr<R and 0<=nc<C and grid[nr][nc]==1):
                        q.append((nr,nc))
                        grid[nr][nc]=2
                        fresh-=1
            
            time+=1
        
        return time if fresh==0 else -1

        