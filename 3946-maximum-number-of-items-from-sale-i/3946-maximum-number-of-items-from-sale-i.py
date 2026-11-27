from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(factor for factor, _ in items)
        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1
            
        multiples_count = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                total = 0
                for m in range(f, max_factor + 1, f):
                    total += freq[m]
                multiples_count[f] = total - 1
                
        dp = [-1] * (budget + 1)
        dp[0] = 0
        
        min_price = float('inf')
        for factor, price in items:
            if price < min_price:
                min_price = price
            if price > budget:
                continue
                
            gain = 1 + multiples_count[factor]
            for c in range(budget, price - 1, -1):
                if dp[c - price] != -1:
                    val = dp[c - price] + gain
                    if val > dp[c]:
                        dp[c] = val
                        
        ans = 0
        for c in range(budget + 1):
            if dp[c] != -1:
                extra_copies = (budget - c) // min_price
                ans = max(ans, dp[c] + extra_copies)
                
        return ans