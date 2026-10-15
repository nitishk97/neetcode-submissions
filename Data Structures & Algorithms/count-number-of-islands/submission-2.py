class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        neighbors = [(-1,0),(0,-1),(0,1),(1,0)]
        queue = deque()
        count=0
        def bfs(queue, grid):
            while queue:
                row, col = queue.popleft()
                grid[row][col] = "#"
                for r, c in neighbors:
                    nr,nc = row+r, col+c
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]=="1":
                        grid[nr][nc]="#"
                        queue.append((nr,nc))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    grid[i][j]="#"
                    queue.append((i,j))
                    bfs(queue, grid)
                    count+=1
        return count
            
        