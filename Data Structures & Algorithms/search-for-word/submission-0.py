class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        neighbors = [(-1,0),(0,1),(1,0),(0,-1)]
        def findword(r,c,idx):
            row,col = r,c
            if idx == len(word):
                return True

            if not (0<=r<=len(board)-1 and 0<=c<=len(board[0])-1) or board[r][c]!= word[idx]:
                return False
            temp = board[r][c]
            board[r][c] = '#'
            for nr, nc in neighbors:
                if findword(row+nr, col+nc, idx+1):
                    return True
            board[r][c]=temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if findword(i, j, 0):
                        return True
        return False              
                    



        