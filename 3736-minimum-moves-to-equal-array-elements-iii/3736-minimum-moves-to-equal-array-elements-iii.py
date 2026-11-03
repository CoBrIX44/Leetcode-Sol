class Solution:
    def minMoves(self, nums: List[int]) -> int:
        biggest = max(nums)
        return biggest * len(nums) - sum(nums)