class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ans = []

        i=0
        for i in range(n):
            if intervals[i][0] > newInterval[1]:
                ans.append(newInterval)
                return ans + intervals[i:n]

            elif intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])

            else:
                newInterval = [min(intervals[i][0],newInterval[0]), 
                            max(intervals[i][1],newInterval[1])]

        ans.append(newInterval)
        return ans
        

        

        


