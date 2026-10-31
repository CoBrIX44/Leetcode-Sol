class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        R = [[-1] * n for _ in range(m)]
        D = [[-1] * n for _ in range(m)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    R[i][j] = i * n + j
                    D[i][j] = i * n + j
                else:
                    R[i][j] = D[i + 1][j] if i + 1 < m else -1
                    D[i][j] = R[i][j + 1] if j + 1 < n else -1
        
        dp = [0] * (m * n)
        dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                cur = dp[i * n + j]
                if cur == 0 or grid[i][j] == 1:
                    continue
                if j + 1 < n:
                    t = R[i][j + 1]
                    if t != -1:
                        dp[t] = (dp[t] + cur) % MOD
                if i + 1 < m:
                    t = D[i + 1][j]
                    if t != -1:
                        dp[t] = (dp[t] + cur) % MOD
        
        return dp[m * n - 1] % MOD