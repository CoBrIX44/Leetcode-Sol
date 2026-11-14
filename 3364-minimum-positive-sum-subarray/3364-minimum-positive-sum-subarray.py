class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        best = float('inf')
        
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                length = j - i + 1
                if l <= length <= r and total > 0:
                    best = min(best, total)
        
        return -1 if best == float('inf') else best