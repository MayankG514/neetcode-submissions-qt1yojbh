class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()

        def dfs(i,res,t):
            if t == target:
                ans.append(res.copy())
                return
            
            if i>=n or t>target:
                return
            res.append(candidates[i])
            dfs(i+1,res, candidates[i]+t)
            res.pop()

            while i<n-1 and candidates[i]==candidates[i+1]:
                i+=1

            dfs(i+1, res, t)
        
        dfs(0,[],0)

        return ans