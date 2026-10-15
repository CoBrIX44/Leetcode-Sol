class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        row = [0] * n
        row[0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    row[j] = 0
                elif j > 0:
                    row[j] += row[j - 1]
        
        return row[n - 1]