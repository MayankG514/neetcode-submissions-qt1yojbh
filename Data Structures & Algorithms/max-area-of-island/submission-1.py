class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        maxA = 0


        def bfs(r,c):
            q = collections.deque()
            grid[r][c] = 0
            q.append((r,c))

            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            area = 1
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr, col+dc
                    if (nr<R and nr>=0 
                        and nc>=0 and 
                        nc<C and grid[nr][nc]==1):
                        q.append((nr,nc))
                        grid[nr][nc]=0
                        area+=1
            return area
    
        for i in range(R):
            for j in range(C):
                if (grid[i][j]==1):
                    area = bfs(i,j)
                    maxA = max(maxA,area)
        return maxA
