class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()
        n = len(candidates)

        def backtracking(i,arr,arrTotal):
            if arrTotal == target:
                res.append(arr.copy())
                return     

            if arrTotal>target or i == n:
                return

            arr.append(candidates[i])
            backtracking(i+1,arr,arrTotal+candidates[i])
            arr.pop()


            while i+1<n and candidates[i]==candidates[i+1]:
                i+=1
            backtracking(i+1, arr, arrTotal)
        
        backtracking(0,[],0)
        return res

# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         candidates.sort()

#         def dfs(i, cur, total):
#             if total == target:
#                 res.append(cur.copy())
#                 return
#             if total > target or i == len(candidates):
#                 return

            # cur.append(candidates[i])
            # dfs(i + 1, cur, total + candidates[i])
            # cur.pop()


        #     while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
        #         i += 1
        #     dfs(i + 1, cur, total)

        # dfs(0, [], 0)
        # return res

