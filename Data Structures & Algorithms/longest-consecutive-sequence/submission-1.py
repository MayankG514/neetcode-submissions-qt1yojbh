class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maxL=0
        n = len(nums)

        for i in range(n):
            if nums[i]-1 not in nums:
                s = nums[i]
                l = 0

                while s in nums:
                    s+=1
                    l+=1
                maxL = max(l,maxL)
        return maxL