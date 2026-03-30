class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res =[]
        stack =[]
        currentString =""
        
        def dfs(openb,closeb):
            if openb==closeb==n:
                res.append("".join(stack))
                return
            
            if closeb < openb:
                stack.append(')')
                dfs(openb,closeb+1)
                stack.pop()
            
            if openb < n:
                stack.append('(')
                dfs(openb+1,closeb)
                stack.pop()
            
        dfs(0,0)
        return res
