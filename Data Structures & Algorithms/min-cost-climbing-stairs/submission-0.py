class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCostArr = [0]*(n+1)

        if n < 2:
            return 0
        
        minCostArr[-2] = cost[n-1]
        
        for i in range(len(minCostArr)-3,-1,-1):
            minCostArr[i] = min((cost[i]+minCostArr[i+1]), (cost[i]+minCostArr[i+2]))
        
        print(minCostArr)
        
        return min(minCostArr[0],minCostArr[1])