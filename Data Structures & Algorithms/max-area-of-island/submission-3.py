class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        R,C = len(grid), len(grid[0])
        visit = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        
        def calArea(r,c):
            q = collections.deque()
            grid[r][c]=0
            q.append((r,c))
            area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (0<=nr<R and 0<=nc<C and (nr,nc) and grid[nr][nc]==1):
                        area+=1
                        grid[nr][nc] = 0
                        q.append((nr,nc))

            return area

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    area = calArea(r,c)
                    ans = max(ans,area)
        return ans
