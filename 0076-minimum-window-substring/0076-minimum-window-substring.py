class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        missing = len(t) 
        left = 0
        best_start, best_len = 0, float('inf')
        
        for right in range(len(s)):
            c = s[right]
            if c in need:
                if need[c] > 0:
                    missing -= 1
                need[c] -= 1
            
            while missing == 0:
                if right - left + 1 < best_len:
                    best_start = left
                    best_len = right - left + 1
                
                lc = s[left]
                if lc in need:
                    need[lc] += 1
                    if need[lc] > 0:
                        missing += 1
                left += 1
        
        return "" if best_len == float('inf') else s[best_start:best_start + best_len]