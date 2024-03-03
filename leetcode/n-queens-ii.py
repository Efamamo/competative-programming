class Solution:
    def totalNQueens(self, n: int) -> int:
        state=[['.'] * n for _ in range(n)]
        visited_cols=set()
        visited_diagonals=set()
        visited_antidiagonals=set()
        
        res=set()
        def backtrack(r):
            if r==n:
                res.add(map('#'.join, map(''.join, state)))
                return
                        
            for c in range(n):
                if not(c in visited_cols or (r-c) in visited_diagonals or (r+c) in visited_antidiagonals):
                    visited_cols.add(c)
                    visited_diagonals.add(r-c)
                    visited_antidiagonals.add(r+c)
                    state[r][c]='Q'
                    backtrack(r+1)
                    
                    visited_cols.remove(c)
                    visited_diagonals.remove(r-c)
                    visited_antidiagonals.remove(r+c)
                    state[r][c]='.'
                        
        backtrack(0)
        return len(res)