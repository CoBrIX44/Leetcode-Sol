class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
        
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
        
        dp = [set() for _ in range(n)]
        dp[0] = {1}  
        
        for j in range(1, n):
            prev = dp[j-1]
            if not prev:
                dp[j] = set()
                continue
            delta = 1 if grid[0][j] == '(' else -1
            dp[j] = {b + delta for b in prev if b + delta >= 0}
        
        for i in range(1, m):
            new_dp = [set() for _ in range(n)]
            delta = 1 if grid[i][0] == '(' else -1
            new_dp[0] = {b + delta for b in dp[0] if b + delta >= 0}
            
            for j in range(1, n):
                delta = 1 if grid[i][j] == '(' else -1
                balances = set()
                
                for b in dp[j]:
                    nb = b + delta
                    if nb >= 0:
                        balances.add(nb)
                
                for b in new_dp[j-1]:
                    nb = b + delta
                    if nb >= 0:
                        balances.add(nb)
                new_dp[j] = balances
            
            dp = new_dp
        
        return 0 in dp[n-1]