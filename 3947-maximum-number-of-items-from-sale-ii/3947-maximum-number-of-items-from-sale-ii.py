from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        min_price = float('inf')
        
        for factor, price in items:
            freq[factor] += 1
            if price < min_price:
                min_price = price
                
        multiples_count = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f] > 0:
                total = 0
                for m in range(f, n + 1, f):
                    total += freq[m]
                multiples_count[f] = total
                
        two_copy_prices = []
        for factor, price in items:
            max_pairs = multiples_count[factor] - 1
            if max_pairs > 0:
                two_copy_prices.append((price, max_pairs))
                
        two_copy_prices.sort()
        
        total_copies = 0
        
        limit = 2 * min_price
        for price, count in two_copy_prices:
            if price > limit or budget < price:
                break
            take = min(count, budget // price)
            total_copies += take * 2
            budget -= take * price
            
        total_copies += budget // min_price
        
        return total_copies