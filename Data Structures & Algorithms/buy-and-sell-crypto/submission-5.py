class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l,r = 0,1
        n = len(prices)

        while r<n:
            p = prices[r]-prices[l]

            if p > 0:
                maxP = max(p,maxP)
            else:
                l = r
            r+=1
        return maxP
