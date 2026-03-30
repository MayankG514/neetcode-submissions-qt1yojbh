class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lprod,rprod =[1]*n,[1]*n
        for i in range(1,n):
            lprod[i] = lprod[i-1]*nums[i-1]

        for i in range(n-2,-1,-1):
            rprod[i] = rprod[i+1]*nums[i+1]
        
        ans = [1]*n
        for i in range(0,n):
            ans[i] = lprod[i]*rprod[i]
        return ans