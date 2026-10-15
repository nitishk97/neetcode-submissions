class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        neighbors = [(-1,0),(0,1),(1,0),(0,-1)]
        def bfs(i,j):
            count=1
            grid[i][j]="#"
            queue = deque([(i,j)])

            while queue:
                row, col = queue.popleft()
                for nr, nc in neighbors:
                    nrow, ncol = row+nr, col+nc
                    if 0<=nrow<len(grid) and 0<=ncol<len(grid[0]) and grid[nrow][ncol]==1:
                        count+=1
                        grid[nrow][ncol]="#"
                        queue.append((nrow, ncol))
            return count
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    curr = bfs(i,j)
                    result = max(result, curr)
        return result

        