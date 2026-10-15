from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        pos_diag = set()
        neg_diag = set()
        
        def dfs(idx, board):
            if idx == n:
                res.append(["".join(row) for row in board])
                return 
                
            for i in range(n):
                if i in cols or idx + i in pos_diag or idx - i in neg_diag:
                    continue
                    
                board[idx][i] = "Q"
                cols.add(i)
                pos_diag.add(idx + i)
                neg_diag.add(idx - i)
                
                dfs(idx + 1, board)
                
                # FIX: Explicitly remove the exact values you added
                cols.remove(i)
                pos_diag.remove(idx + i)
                neg_diag.remove(idx - i)
                board[idx][i] = "."
                
        dfs(0, board)
        return res
