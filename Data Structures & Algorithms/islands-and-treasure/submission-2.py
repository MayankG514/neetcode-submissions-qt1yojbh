class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R,C = len(grid), len(grid[0])
        q = collections.deque()
        INF = 2**31 - 1
        directions = [[-1,0],[0,-1],[1,0],[0,1]]

        for r in range(R):
            for c in range(C):
                if grid[r][c]==0:
                    q.append((r,c))
        
        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                row, col = r+dr, c+dc
                if 0<=row<R and 0<=col<C and grid[row][col]==INF:
                    grid[row][col] = 1 + grid[r][c]
                    q.append((row,col))
        

