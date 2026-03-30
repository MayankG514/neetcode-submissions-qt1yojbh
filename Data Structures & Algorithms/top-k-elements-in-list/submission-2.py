class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            d[nums[i]] = 1 + d.get(nums[i],0)
        
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

        ans = []
        for key,val in d.items():
            ans.append(key)
        
        return ans[:k]