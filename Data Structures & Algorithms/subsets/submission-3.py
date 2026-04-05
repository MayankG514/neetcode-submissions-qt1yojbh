class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        n = len(nums)
        ans = []
        res = []
        
        def dfs(i,res):
            if i==n:
                ans.append(res.copy())
                return
            
            if i > n:
                return
            
            res.append(nums[i])
            dfs(i+1,res)
            res.pop()
            dfs(i+1,res)
        
        dfs(0,[])
        return ans
                    
