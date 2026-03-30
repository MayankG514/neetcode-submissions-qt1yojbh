class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        n=len(nums)
        maxL = 0
        for i in range(0,n):
            if nums[i]-1 not in nums:
                s= nums[i]
                l=0
                while s in nums:
                    l+=1
                    s+=1
                maxL = max(l,maxL)
        return maxL
