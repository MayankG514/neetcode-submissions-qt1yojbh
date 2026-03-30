class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxL = 0

        for i in range(len(nums)):
            if nums[i]-1 not in nums:
                s = nums[i] 
                l = 0
                while s in nums:
                    s+=1
                    l+=1
                maxL = max(maxL,l)
        return maxL