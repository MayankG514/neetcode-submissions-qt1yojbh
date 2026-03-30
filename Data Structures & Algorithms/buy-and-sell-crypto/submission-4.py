class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        n = len(prices)
        l=0
        r=1

        while r<n:
            p = prices[r]-prices[l]
            if p > 0:
                maxP = max(maxP,p)
            else:
                l = r
            r+=1
        return maxP
