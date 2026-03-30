class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        ans = r
        while l<=r:
            totalTime = 0
            m = l + ((r-l)//2)

            for n in piles:
                totalTime+= math.ceil(float(n)/m)

            if totalTime > h:
                l = m+1
            else:
                ans = m
                r = m-1
        return ans