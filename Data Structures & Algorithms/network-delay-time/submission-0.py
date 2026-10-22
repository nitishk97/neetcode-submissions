class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u,v,t in times:
            adj[u].append((t,v))
        queue = [(0,k)]
        result = 0
        visited = set()
        while queue:
            time, node = heapq.heappop(queue)
            if node in visited:
                continue
            result = time
            visited.add(node)
            for edge_time, edge_node in adj[node]:
                if edge_node not in visited:
                    heapq.heappush(queue, (time+edge_time, edge_node))
        if len(visited)==n:
                return result
        return -1





