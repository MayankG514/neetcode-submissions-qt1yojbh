class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res =[]

        def backtracking(i,arr,sumofArr):
            if sumofArr>target or i>=len(nums):
                return
            
            if sumofArr==target:
                res.append(arr.copy())
                return

            arr.append(nums[i])
            backtracking(i,arr,sumofArr+nums[i])
            arr.pop()
            backtracking(i+1,arr,sumofArr)

        backtracking(0,[],0)
        return res
            
            