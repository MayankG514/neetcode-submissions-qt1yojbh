class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def dfs(i,res):
            if i==n:
                ans.append(res.copy())
                return
            
            res.append(nums[i])
            dfs(i+1,res)
            res.pop()
            dfs(i+1,res)
        
        dfs(0,[])
        return ans
            