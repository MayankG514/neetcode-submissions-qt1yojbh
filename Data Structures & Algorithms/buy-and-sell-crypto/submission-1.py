class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        n=len(prices)
        maxP=0
        while r<n:
            if prices[l] < prices[r]:
                prof = prices[r]-prices[l]
                maxP = max(prof,maxP)
            else:
                l=r
            r+=1

        return maxP
            