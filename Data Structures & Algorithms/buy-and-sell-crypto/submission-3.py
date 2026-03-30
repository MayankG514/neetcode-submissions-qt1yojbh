class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 
        n = len(prices)
        if n==0 or n==1:
            return 0

        l = 0
        r = 1

        while r<n:
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                maxP = max(profit,maxP)
            else:
                l = r
            r+=1
        return maxP
            

