class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = 1001
        for i in range(len(nums)):
            ans = min(ans,nums[i])
        return ans
        # time complexity -> O(n)
        # space -> O(1)