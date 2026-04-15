class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for n in nums:
            hmap[n] = 1 + hmap.get(n,0)
        
        heap = []

        for num in hmap.keys():
            heapq.heappush(heap,(hmap[num],num))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []

        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans