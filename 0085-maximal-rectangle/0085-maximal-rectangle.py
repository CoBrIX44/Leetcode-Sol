class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0
        
        for row in matrix:
            for c in range(cols):
                heights[c] = heights[c] + 1 if row[c] == "1" else 0
            
            stack = []
            for i in range(cols + 1):
                while stack and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
        return max_area