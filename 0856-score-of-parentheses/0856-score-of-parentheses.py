class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  
        
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                v = stack.pop()
                score = 2 * v if v > 0 else 1
                stack[-1] += score
        
        return stack[0]