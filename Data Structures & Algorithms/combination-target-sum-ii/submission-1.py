class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(i,res, total):
            if total == target:
                ans.append(res.copy())
                return
            
            if total > target or i>=len(candidates):
                return
            
            res.append(candidates[i])
            dfs(i+1,res,total+candidates[i])

            res.pop()

            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            
            dfs(i+1,res,total)
        
        dfs(0,[],0)

        return ans


        
