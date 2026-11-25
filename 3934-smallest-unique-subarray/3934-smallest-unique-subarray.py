from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        BASE1, MOD1 = 1315423911, 10**9 + 7
        BASE2, MOD2 = 2654435761, 10**9 + 9
        
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        
        for i, val in enumerate(nums):
            pref1[i + 1] = (pref1[i] * BASE1 + val) % MOD1
            pref2[i + 1] = (pref2[i] * BASE2 + val) % MOD2
            pow1[i + 1] = (pow1[i] * BASE1) % MOD1
            pow2[i + 1] = (pow2[i] * BASE2) % MOD2
            
        def has_unique_subarray(length: int) -> bool:
            p1 = pow1[length]
            p2 = pow2[length]
            seen_once = set()
            duplicates = set()
            
            for i in range(n - length + 1):
                h1 = (pref1[i + length] - pref1[i] * p1) % MOD1
                h2 = (pref2[i + length] - pref2[i] * p2) % MOD2
                key = (h1 << 32) | h2
                
                if key in duplicates:
                    continue
                if key in seen_once:
                    seen_once.remove(key)
                    duplicates.add(key)
                else:
                    seen_once.add(key)
                    
            return len(seen_once) > 0

        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique_subarray(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans