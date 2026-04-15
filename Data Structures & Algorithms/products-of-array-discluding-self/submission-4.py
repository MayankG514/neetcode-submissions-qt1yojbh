class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod = 1
        # zero_count = 0 

        # for n in nums:
        #     if n != 0:
        #         prod*= n
        #     else:
        #         zero_count +=1

        # ans = [0] * len(nums)

        # if zero_count > 1:
        #     return ans       

        # for i,n in enumerate(nums):
        #     if zero_count: ans[i] = 0 if n else prod
        #     else: ans[i] = prod // n
        
        # return ans

        # time complexity -> O(n)
        # space complexity -> O(n)

        n = len(nums)
        lprod = [1]*n
        rprod = [1]*n

        for i in range(1,n):
            lprod[i] = lprod[i-1] * nums[i-1]
        
        for i in range(n-2,-1,-1):
            rprod[i] = rprod[i+1] * nums[i+1]
        
        res = []
        for i in range(n):
            res.append(lprod[i]*rprod[i])
        
        return res


        