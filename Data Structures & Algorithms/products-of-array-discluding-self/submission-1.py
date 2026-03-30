class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
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
