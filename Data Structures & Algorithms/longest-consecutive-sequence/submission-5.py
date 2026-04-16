class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxL = 0
        numset = set(nums)


        for i in range(len(nums)):
            if nums[i]-1 not in numset:
                s = nums[i] 
                l = 0
                while (nums[i]+l) in numset:
                    l+=1
                maxL = max(maxL,l)
        return maxL