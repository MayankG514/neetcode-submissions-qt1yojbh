class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        n = len(piles)
        
        while l<=r:
            timeTaken = 0
            m = l + ((r-l)//2)

            for p in piles:
                timeTaken += math.ceil(float(p)/m)
            
            if timeTaken > h:
                l = m+1
            else:
                ans = m
                r = m-1
        return ans