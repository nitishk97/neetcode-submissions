class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        neighbors = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    visited.add((i,j))
                    queue.append((i,j,0))
        while queue:
            row, col, dist = queue.popleft()
            for nr, nc in neighbors:
                nrow, ncol = row+nr, col+nc
                if 0<=nrow<len(grid) and 0<=ncol<len(grid[0]) and (nrow, ncol) not in visited and grid[nrow][ncol]==2147483647:
                    grid[nrow][ncol] = dist+1
                    visited.add((nrow,ncol))
                    queue.append((nrow,ncol, dist+1))                    