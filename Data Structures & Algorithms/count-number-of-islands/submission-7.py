class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R,C = len(grid), len(grid[0])
        visit = set()
        islands = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]


        def dfs(r,c):
            if (r,c) in visit or grid[r][c]=='0':
                return
            
            visit.add((r,c))

            for dr,dc in directions:
                row, col = dr+r, dc+c
                if (0<=row<R and 0<=col<C and grid[row][col]=='1' and (row,col) not in visit):
                    dfs(row,col)
                       


        for r in range(R):
            for c in range(C):
                if (r,c) not in visit and grid[r][c]=='1':
                    dfs(r,c)
                    islands+=1
        
        return islands