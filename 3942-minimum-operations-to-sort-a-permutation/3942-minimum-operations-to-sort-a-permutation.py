class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        best = float('inf')
        
        k = nums[0]
        if all(nums[i] == (i + k) % n for i in range(n)):
            if k == 0:
                best = 0
            else:
        
                best = min(n - k, k + 2)
        
    
        k = n - 1 - nums[0]
        if all(nums[i] == n - 1 - ((i + k) % n) for i in range(n)):
           
            best = min(best, k + 1, n - k + 1)
        
        return -1 if best == float('inf') else best