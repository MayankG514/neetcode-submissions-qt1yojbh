class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        n=len(nums)

        def dfs(i,res):
            if i==n:
                ans.append(res.copy())
                return
            
            res.append(nums[i])
            dfs(i+1,res)

            res.pop()
            while (i+1) < n and nums[i]==nums[i+1]:
                i+=1
            
            dfs(i+1,res)

        dfs(0,[])
        return ans