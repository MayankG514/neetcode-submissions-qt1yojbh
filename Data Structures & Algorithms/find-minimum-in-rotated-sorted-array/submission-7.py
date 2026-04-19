class Solution:
    def findMin(self, nums: List[int]) -> int:
        # ans = 1001
        # for i in range(len(nums)):
        #     ans = min(ans,nums[i])
        # return ans
        # time complexity -> O(n)
        # space -> O(1)
        n = len(nums)

        l,r = 0, n-1
        
        res = nums[0]

        while l<=r:
            if nums[l] < nums[r]:
                res =min(res,nums[l])
                break

            m = l + ((r-l)//2)
            res = min(res,nums[m])

            if nums[m] < nums[r]:
                r = m-1
            elif nums[m] >= nums[l]:
                l = m+1
        
        return res
        