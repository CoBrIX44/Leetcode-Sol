class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        bit_count = [0] * 30
        for num in nums:
            for b in range(30):
                if num & (1 << b):
                    bit_count[b] += 1
        
        total = 0
        for _ in range(k):
            value = 0
            for b in range(30):
                if bit_count[b] > 0:
                    value |= (1 << b)
                    bit_count[b] -= 1
            total += value * value
        
        return total % MOD