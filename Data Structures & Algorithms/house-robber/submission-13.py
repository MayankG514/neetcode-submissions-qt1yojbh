class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        if n==2:
            return max(nums[0],nums[1])
        
        dp = [0]*n

        dp[0] = nums[0]

        for i in range(1,n):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        
        return dp[n-1]
            