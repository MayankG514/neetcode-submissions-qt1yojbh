class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        total=0
        n=len(nums)

        def bt(i,total,res):
            if i>=n or total>target:
                return

            if total == target:
                ans.append(res.copy())
                return
            
            res.append(nums[i])
            bt(i,total+nums[i],res)

            res.pop()
            bt(i+1,total,res)
        
        bt(0,total,[])

        return ans
            

        
