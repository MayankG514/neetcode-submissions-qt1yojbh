class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            distance = -1* ((x**2)+(y**2))
            heapq.heappush(heap,[distance,x,y])
                
        while len(heap) > k:
            heapq.heappop(heap)
        
        res = []
        for h in heap:
            res.append([h[1],h[2]])
        return res
