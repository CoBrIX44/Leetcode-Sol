class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1  
        
        for i in range(len(nums)):
            if nums[i] != i:
                k &= nums[i]
        
        return 0 if k == -1 else k