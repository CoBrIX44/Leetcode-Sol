class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        k = k1 + k2
        
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        
        if sum(diffs) <= k:
            return 0
        
        max_d = max(diffs)
        count = [0] * (max_d + 1)
        for d in diffs:
            count[d] += 1
        
        for d in range(max_d, 0, -1):
            if count[d] == 0:
                continue
            
            if count[d] <= k:
                
                k -= count[d]
                count[d - 1] += count[d]
                count[d] = 0
            else:
                
                count[d - 1] += k
                count[d] -= k
                k = 0
                break
        
        total = 0
        for d in range(max_d + 1):
            total += count[d] * d * d
        
        return total