class Solution:
    def climbStairs(self, n: int) -> int:
        
        # def dfs(i):
        #     if i >= n:
        #         return i==n
        #     return dfs(i+1) + dfs(i+2)
        
        # return dfs(0)

        # time complexity -> O(2**n)

        if n<3:
            return n
        
        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n]

        # time complexity -> O(n)

        
