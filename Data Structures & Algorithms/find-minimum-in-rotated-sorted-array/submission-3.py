class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,h = 0, n-1
        ans = nums[0]

        while l<=h:
            if nums[l]<nums[h]:
                ans = min(ans,nums[l])
                break

            m= l + ((h-l)//2)
            ans = min(ans,nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else:
                h = m-1
        return ans