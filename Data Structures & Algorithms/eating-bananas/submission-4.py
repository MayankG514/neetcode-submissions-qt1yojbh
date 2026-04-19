class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high = 1,max(piles)
        ans = high

        while low<=high:
            m = low + ((high-low)//2)
            t = 0
            for p in piles:
                t+= math.ceil(float(p)/m)
            
            if t>h:
                low = m+1
            elif t<=h:
                ans = m
                high = m-1

        return ans