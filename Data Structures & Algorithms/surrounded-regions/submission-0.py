class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])

        def capture(r,c):
            if (r>=R or c>=C or r<0 or c<0 or board[r][c]!='O'):
                return
            
            board[r][c] = 'T'

            capture(r+1,c)
            capture(r,c+1)
            capture(r-1,c)
            capture(r,c-1)
        
        for r in range(R):
            if board[r][0]=='O':
                capture(r,0)
            if board[r][C-1]=='O':
                capture(r,C-1)

        for c in range(C):
            if board[0][c]=='O':
                capture(0,c)
            if board[R-1][c]=='O':
                capture(R-1,c)
        
        for i in range(R):
            for j in range(C):
                if board[i][j]=='O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'
        