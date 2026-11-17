class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = INF
                for d in range(1, length):
                    if length % d != 0:
                        continue
                    changes = 0
                    for g in range(d):
                        idx = list(range(i + g, j + 1, d))
                        a, b = 0, len(idx) - 1
                        while a < b:
                            if s[idx[a]] != s[idx[b]]:
                                changes += 1
                            a += 1
                            b -= 1
                    best = min(best, changes)
                cost[i][j] = best

        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for i in range(1, n + 1):
                for j in range(i - 1):  
                    if dp[p - 1][j] < INF and cost[j][i - 1] < INF:
                        dp[p][i] = min(dp[p][i], dp[p - 1][j] + cost[j][i - 1])

        return dp[k][n]