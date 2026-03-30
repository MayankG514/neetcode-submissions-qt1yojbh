class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])

        lr, hr = 0, r-1
        R = -1

        while lr<=hr:
            m = lr + ((hr-lr)//2)

            if target < matrix[m][0]:
                hr = m-1
            elif target > matrix[m][-1]:
                lr = m+1
            else:
                break
        if not (lr<=hr):
            return False
        
        R = (lr+hr)//2

        l,r = 0, c-1
        while l<=r:
            m = l + ((r-l)//2)

            if matrix[R][m] < target:
                l = m+1
            elif matrix[R][m] > target:
                r = m-1
            elif matrix[R][m]==target:
                return True

        return False
                
