class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        l=r=0
        ans = []

        while r < n:
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                ans.append(nums[q[0]])
                l+=1

            r+=1
        return ans

        
        # ans = []
        # for i in range(0,n-k+1):
        #     maxE = max(nums[i:i+k])
        #     ans.append(maxE)
        # return ans