class Solution:

    def calProfit(self, nums) -> int:
        dp = [0]*(len(nums))
        if len(nums) == 1:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        
        return dp[len(nums)-1]



    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        if n ==1:
            return nums[0]
        
        return max(self.calProfit(nums[1:]), self.calProfit(nums[:-1]))
        

        
        
        
