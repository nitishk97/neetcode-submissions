class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = [[False]*len(heights[0]) for _ in range(len(heights))]
        atlantic = [[False]*len(heights[0]) for _ in range(len(heights))]

        rows = len(heights)
        cols = len(heights[0])

        neighbors = [(-1,0),(1,0),(0,-1),(0,1)]

        pac = deque()
        atl = deque()
        for c in range(cols):
            pac.append((0,c))
            atl.append((rows-1, c))
        for r in range(rows):
            pac.append((r, 0))
            atl.append((r, cols-1))
        def bfs(source, ocean):
            while source:
                row, col = source.popleft()
                ocean[row][col]=True
                for nr, nc in neighbors:
                    nrow, ncol = row+nr, col+nc
                    if 0<=nrow<rows and 0<=ncol<cols and not ocean[nrow][ncol]:
                        if heights[nrow][ncol]>=heights[row][col]:
                            source.append((nrow, ncol))
        bfs(pac, pacific)
        bfs(atl, atlantic)

        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r,c])
        return result

            

