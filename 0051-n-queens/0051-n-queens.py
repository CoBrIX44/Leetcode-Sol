class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        cols = set()
        diag1 = set()  
        diag2 = set()  
        queens = []    
        
        def backtrack(r):
            if r == n:
                board = []
                for c in queens:
                    board.append('.' * c + 'Q' + '.' * (n - c - 1))
                result.append(board)
                return
            
            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue
                
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                queens.append(c)
                
                backtrack(r + 1)
                
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)
                queens.pop()
        
        backtrack(0)
        return result