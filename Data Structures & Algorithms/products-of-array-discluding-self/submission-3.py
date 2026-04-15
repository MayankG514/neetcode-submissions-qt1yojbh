class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        zero_count = 0 

        for n in nums:
            if n != 0:
                prod*= n
            else:
                zero_count +=1

        ans = [0] * len(nums)

        if zero_count > 1:
            return ans       


        for i,n in enumerate(nums):
            if zero_count: ans[i] = 0 if n else prod
            else: ans[i] = prod // n
        
        return ans

        