class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        queue = [(0,0)]
        visited = set()
        result = 0
        while queue:
            dist, node = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            result+=dist
            for dis, nnode in adj[node]:
                if nnode not in visited:
                    heapq.heappush(queue,(dis, nnode))
        return result