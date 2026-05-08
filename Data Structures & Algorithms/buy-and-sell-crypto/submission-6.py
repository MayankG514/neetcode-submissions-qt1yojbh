class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)        
        l,r = 0,1
        ans = 0

        while r<n:
            profit = prices[r]-prices[l]

            if profit > 0:
                ans = max(profit,ans)
            
            else:
                l = r

            r+=1
        
        return ans

