class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])

        t,b = 0,r-1

        while t<=b:
            R = (t+b)//2
            if target< matrix[R][0]:
                b = R-1
            elif target>matrix[R][-1]:
                t = R+1
            else:
                break
        
        if not (t<=b):
            return False

        row = (t+b)//2

        l,r = 0,c-1

        while l<=r:
            m = (l+r)//2

            if matrix[row][m]<target:
                l = m+1
            elif matrix[row][m]>target:
                r = m-1
            else:
                return True
        return False
