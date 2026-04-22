class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res = nums[0]
        # for i in range(len(nums)):
        #     cur = nums[i]
        #     res = max(res,nums[i])
        #     for j in range(i+1, len(nums)):
        #         cur *= nums[j]
        #         res = max(res,cur)
        # return res

        # time complexity -> O(n**2)
        # space -> O(1)
        res = nums[0]
        currMax, currMin = 1,1

        for i in range(len(nums)):
            if nums[i]==0:
                currMax, currMin = 1,1 
                res = max(res,0)
                continue
            t = currMax
            currMax = max((nums[i]*currMin), (nums[i]*currMax), nums[i])
            currMin = min((nums[i]*currMin), (nums[i]*t), nums[i])
            res = max(currMax, res)
        return res
            
