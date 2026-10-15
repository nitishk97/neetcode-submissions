class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result = 0
        queue = deque()
        neighbors = [(-1,0),(1,0),(0,-1),(0,1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j,0))
        while queue:
            row, col, time = queue.popleft()
            result = time
            for nr, nc in neighbors:
                nrow, ncol = row+nr, col+nc
                if 0<=nrow<len(grid) and 0<=ncol<len(grid[0]) and grid[nrow][ncol]==1:
                    grid[nrow][ncol]=2
                    queue.append((nrow, ncol, time+1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return result

        