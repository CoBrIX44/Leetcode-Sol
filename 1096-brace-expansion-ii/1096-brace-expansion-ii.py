class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)
        
        def parse_union(i):
            groups = []
            while True:
                s, i = parse_concat(i)
                groups.append(s)
                if i < n and expression[i] == ',':
                    i += 1
                else:
                    break
            result = set()
            for g in groups:
                result |= g
            return result, i
        
        def parse_concat(i):
            result = {''}
            while i < n and expression[i] not in ',}':
                if expression[i] == '{':
                    s, i = parse_union(i + 1)
                    i += 1  
                else:
                    s = {expression[i]}
                    i += 1
                result = {a + b for a in result for b in s}
            return result, i
        
        words, _ = parse_union(0)
        return sorted(words)