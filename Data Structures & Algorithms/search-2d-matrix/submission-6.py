class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])

        t,b = 0,r-1

        while t<=b:
            mr = t + ((b-t)//2)

            if matrix[mr][0] > target:
                b = mr-1
            elif matrix[mr][-1] < target:
                t = mr+1
            else:
                break
        
        if not (t<=b):
            return False
        
        rowFound = (t+b)//2
        l,r = 0,c-1

        while l<=r:
            m = l + ((r-l)//2)

            if matrix[rowFound][m] == target:
                return True
            elif matrix[rowFound][m] > target:
                r = m-1
            elif matrix[rowFound][m] < target:
                l = m+1
        return False
