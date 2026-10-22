class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            value = matrix[mid // n][mid % n]
            
            if value == target:
                return True
            elif value < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return False