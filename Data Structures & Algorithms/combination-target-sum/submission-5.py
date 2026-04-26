class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)

        def dfs(i,res,t):
            if t == target:
                ans.append(res.copy())
                return
            
            if i>=n or t > target:
                return
            
            res.append(nums[i])
            dfs(i,res,t+nums[i])
            res.pop()
            dfs(i+1,res,t)
        
        dfs(0,[],0)

        return ans