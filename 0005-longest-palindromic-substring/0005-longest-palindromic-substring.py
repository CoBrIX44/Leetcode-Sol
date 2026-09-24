class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        start, max_len = 0, 1
        
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  
        
        for i in range(len(s)):
            len1 = expand(i, i)       
            len2 = expand(i, i + 1)   
            curr_max = max(len1, len2)
            
            if curr_max > max_len:
                max_len = curr_max
                start = i - (curr_max - 1) // 2
        
        return s[start:start + max_len]