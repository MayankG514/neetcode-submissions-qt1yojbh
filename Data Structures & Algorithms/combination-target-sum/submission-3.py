class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        res = []
        total = 0
        n = len(nums)

        def dfs(i, total,res):
            if i>=n or total > target:
                return
            
            if total == target:
                ans.append(res.copy())
                return
            
            res.append(nums[i])
            dfs(i,total+nums[i],res)

            res.pop()
            dfs(i+1, total,res)
        
        dfs(0,total,[])
        return ans