class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        neighbor = [(-1,0),(0,1),(0,-1),(1,0)]
        ROW = len(grid[0])
        COL = len(grid)
        queue = [(grid[0][0],0,0)]
        result = -1
        visited = set()
        while queue:
            dist, row, col = heapq.heappop(queue)
            result = dist
            if row==len(grid[0])-1 and col==len(grid)-1:
                return result
            if (row,col) in visited:
                continue
            visited.add((row, col))
            for nr, nc in neighbor:
                nrow, ncol = row+nr, col+nc
                if (nrow, ncol) not in visited and 0<=nrow<ROW and 0<=ncol<COL:
                    if grid[nrow][ncol]>dist:
                        heapq.heappush(queue, (grid[nrow][ncol],nrow,ncol))
                    else:
                        heapq.heappush(queue, (dist, nrow, ncol))
        return result   


