class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        n = len(words)
        i = 0
        
        while i < n:
            line_length = len(words[i])
            j = i + 1
            
            while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1
            
            num_words = j - i
            total_spaces = maxWidth - line_length
            
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                gaps = num_words - 1
                base_spaces, extra_spaces = divmod(total_spaces, gaps)
                
                line_parts = []
                for k in range(i, j - 1):
                    line_parts.append(words[k])
                    spaces = base_spaces + (1 if (k - i) < extra_spaces else 0)
                    line_parts.append(" " * spaces)
                
                line_parts.append(words[j - 1])
                line = "".join(line_parts)
            
            result.append(line)
            i = j
            
        return result