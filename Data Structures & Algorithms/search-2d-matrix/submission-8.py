class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R,C = len(matrix), len(matrix[0])

        lr, hr = 0, R-1
        rowFound = -1

        while lr<=hr:
            mr = lr + ((hr-lr)//2)

            if target < matrix[mr][0]:
                hr = mr-1
            elif target > matrix[mr][C-1]:
                lr = mr+1
            else:
                rowFound = mr
                break
        
        if rowFound == -1:
            return False
        
        l,h = 0, C-1
        while l<=h:
            m = l+((h-l)//2)

            if matrix[rowFound][m] > target:
                h = m-1
            elif matrix[rowFound][m] < target:
                l = m+1
            else:
                return True
        
        return False