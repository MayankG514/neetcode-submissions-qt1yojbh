class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        res = []

        for i in range(len(nums)):
            t = target - nums[i]
            if t in hmap:
                res.append(hmap[t])
                res.append(i)
                return res
            hmap[nums[i]] = i
        return []

