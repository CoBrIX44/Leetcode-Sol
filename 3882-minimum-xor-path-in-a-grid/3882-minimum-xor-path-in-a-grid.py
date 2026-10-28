class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [set() for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                if i == 0 and j == 0:
                    dp[j] = {v}
                    continue
                
                new_set = set()
                if i > 0:
                    for x in dp[j]:     
                        new_set.add(x ^ v)
                if j > 0:
                    for x in dp[j - 1]:  
                        new_set.add(x ^ v)
                dp[j] = new_set
        
        return min(dp[n - 1])