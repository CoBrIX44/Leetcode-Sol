class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        best = need1 * cost1 + need2 * cost2
        low, high = min(need1, need2), max(need1, need2)
        high_cost = cost1 if need1 > need2 else cost2
        best = min(best, low * costBoth + (high - low) * min(high_cost, costBoth))
        best = min(best, high * costBoth)
        
        return best