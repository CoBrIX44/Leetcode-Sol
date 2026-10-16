class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [0] * n
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    row[j] = grid[0][0]
                elif i == 0:
                    row[j] = row[j - 1] + grid[i][j]
                elif j == 0:
                    row[j] = row[j] + grid[i][j]
                else:
                    row[j] = min(row[j], row[j - 1]) + grid[i][j]
        
        return row[n - 1]