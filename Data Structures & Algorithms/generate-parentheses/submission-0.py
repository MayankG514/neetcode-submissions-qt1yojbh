class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res =[]

        def backtrack(open_N,close_N):
            if open_N==close_N==n:
                res.append("".join(stack))
            
            if open_N < n:
                stack.append("(")
                backtrack(open_N+1,close_N)
                stack.pop()
            
            if close_N < open_N:
                stack.append(")")
                backtrack(open_N,close_N+1)
                stack.pop()
        backtrack(0,0)

        return res
        