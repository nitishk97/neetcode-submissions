class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        visited = set()
        queue = deque()
        for r in range(rows):
            if board[r][0]=="O":
                queue.append((r,0))
                visited.add((r,0))
            if board[r][cols-1]=="O":
                queue.append((r, cols-1))
                visited.add((r,cols-1))
        for c in range(cols):
            if board[0][c]=="O":
                queue.append((0,c))
                visited.add((0,c))
            if board[rows-1][c]=="O":
                visited.add((rows-1,c))
                queue.append((rows-1, c))

        neighbors = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            row, col = queue.popleft()
            for nr, nc in neighbors:
                nrow, ncol = row+nr, col+nc
                if 0<=nrow<rows and 0<=ncol<cols and (nrow, ncol) not in visited and board[nrow][ncol]=="O":
                    queue.append((nrow, ncol))
                    visited.add((nrow, ncol))
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and (r,c) not in visited:
                    board[r][c]="X"
            