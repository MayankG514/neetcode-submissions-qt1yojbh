class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        n = len(nums)

        l,r = 0,n-1

        while l<=r:
            if nums[l]<nums[r]:
                ans = min(ans,nums[l])
                break
            m = l + ((r-l)//2)
            ans = min(nums[m],ans)

            if nums[m] < nums[r]:
                 r = m-1
            else:
                l = m+1
        return ans