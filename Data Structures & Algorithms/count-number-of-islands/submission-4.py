class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        directions = [[-1,0],[0,1],[0,-1],[1,0]]
        R,C = len(grid), len(grid[0])
        
        def dfs(r,c):
            if (r,c) in visit or r<0 or r>=R or c<0 or c>=C or grid[r][c]=="0":
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r+dr, c+dc)        

        islands = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j]=="1":
                    dfs(i,j)
                    islands+=1
        return islands

