class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            
            ok = True
            prev_max = float('-inf')
            
            for start in range(0, n, k):
                block = nums[start:start + k]
                
                descents = 0
                for i in range(k - 1):
                    if block[i] > block[i + 1]:
                        descents += 1
                if block[-1] > block[0]:
                    descents += 1
                
                if descents > 1:
                    ok = False
                    break
                
                if min(block) < prev_max:
                    ok = False
                    break
                prev_max = max(block)
            
            if ok:
                total += k
        
        return total