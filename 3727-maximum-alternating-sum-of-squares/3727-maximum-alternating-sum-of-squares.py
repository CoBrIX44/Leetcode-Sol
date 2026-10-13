class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(x * x for x in nums)
        n = len(nums)
        minus_count = n // 2  
        
        total = sum(squares[minus_count:]) - sum(squares[:minus_count])
        return total