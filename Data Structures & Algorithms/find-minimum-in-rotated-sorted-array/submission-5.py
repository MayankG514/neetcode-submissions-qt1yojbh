class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        ans = nums[0]

        while l<=r:
            if nums[l] < nums[r]:
                ans = min(nums[l],ans)
                break

            m = l + ((r-l)//2)
            ans = min(ans,nums[m])

            if nums[l] <= nums[m]:
                l = m+1
            elif nums[m] < nums[r]:
                r = m-1
        return ans
