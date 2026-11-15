class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odd_prefix = 0
        even_prefix = 1  
        parity = 0
        result = 0
        
        for x in arr:
            parity = (parity + x) % 2
            if parity == 1:
                result += even_prefix
                odd_prefix += 1
            else:
                result += odd_prefix
                even_prefix += 1
        
        return result % MOD