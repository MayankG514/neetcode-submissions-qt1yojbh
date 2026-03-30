class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows-1

        while top<=bottom:
            mRow = (top+bottom)//2
            if target < matrix[mRow][0]:
                bottom = mRow - 1
            elif target > matrix[mRow][-1]:
                top = mRow + 1
            else:
                break
        
        if not (top<=bottom):
            return False
        
        R = (top + bottom)//2

        l, h = 0, cols-1
        
        while l<=h:
            m = (l+h)//2
            if target == matrix[R][m]:
                return True
            elif target < matrix[R][m]:
                h = m - 1
            elif target > matrix[R][m]:
                l = m + 1

        return False