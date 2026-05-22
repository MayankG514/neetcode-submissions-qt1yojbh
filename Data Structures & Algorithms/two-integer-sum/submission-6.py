class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        res = []

        for i,n in enumerate(nums):
            d = target - n
            if d in hm:
                res.append(hm[d])
                res.append(i)
                return res
            hm[n] = i
        
        