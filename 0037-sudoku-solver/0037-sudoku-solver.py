class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                box_idx = (r // 3) * 3 + (c // 3)
                if val == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
        
        def backtrack(idx):
            if idx == len(empties):
                return True
            
            r, c = empties[idx]
            box_idx = (r // 3) * 3 + (c // 3)
            
            for d in '123456789':
                if d in rows[r] or d in cols[c] or d in boxes[box_idx]:
                    continue
                
                board[r][c] = d
                rows[r].add(d)
                cols[c].add(d)
                boxes[box_idx].add(d)
                
                if backtrack(idx + 1):
                    return True
                
                board[r][c] = '.'
                rows[r].remove(d)
                cols[c].remove(d)
                boxes[box_idx].remove(d)
            
            return False
        
        backtrack(0)