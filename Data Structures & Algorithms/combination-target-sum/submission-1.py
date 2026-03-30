class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        arrTotal =0 
        def backtrack(i,arr,arrTotal):
            if i>=n or arrTotal>target:
                return
            
            if arrTotal==target:
                res.append(arr.copy())
                return
            

            arr.append(nums[i])
            backtrack(i,arr,arrTotal+nums[i])
            arr.pop()
            backtrack(i+1,arr,arrTotal)

        backtrack(0,[],0)

        return res
