class Solution:
    def minMoves(self, nums: list[int]) -> int:
        smallest = min(nums)
        return sum(nums) - smallest * len(nums)