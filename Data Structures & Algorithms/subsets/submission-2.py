class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        res = []
        def dfs(i):
            if i>=n:
                ans.append(res.copy())
                return
            res.append(nums[i])
            dfs(i+1)

            res.pop()
            dfs(i+1)
        dfs(0)

        return ans
