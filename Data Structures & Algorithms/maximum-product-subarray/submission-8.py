class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1,1
        res = nums[0]

        for i in range(len(nums)):
            if nums[i]==0:
                currMax,currMin = 1,1
                res = max(res,0)
                continue

            t = currMax
            currMax = max((nums[i]*currMax),(nums[i]*currMin),nums[i])
            currMin = min((nums[i]*currMin),(nums[i]*t),nums[i])
            res = max(currMax,res)
        
        return res