class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        newLen = 2*n
        st = []

        def dfs(openB,closeB):
            if openB==closeB==n:
                ans.append("".join(st))
                return
            
            if openB < n:
                st.append('(')
                dfs(openB+1,closeB)
                st.pop()
            
            if closeB < openB:
                st.append(')')
                dfs(openB,closeB+1)
                st.pop()
        
        dfs(0,0)
        return ans
