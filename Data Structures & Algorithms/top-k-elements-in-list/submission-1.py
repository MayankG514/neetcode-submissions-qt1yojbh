class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i],0) +1
        
        d_new = dict(sorted(d.items(), key= lambda item: item[1], reverse=True))
        # print(d_new)
        ans = [] 

        for key,val in d_new.items():
            ans.append(key)

        return ans[:k]