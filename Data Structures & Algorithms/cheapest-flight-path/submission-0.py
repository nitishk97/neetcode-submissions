class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #cheapest use dijkstra's but if crossed k stops..delete that path and find next chepest below K stops
        #build adjacency list to traverse graph 
        adj = {i:[] for i in range(n)}
        for u,v,price in flights:
            adj[u].append((price, v))
        queue = [(0, 0, src)] #price, stops, node
        stops_to_node = [float("inf")]*n
        while queue:
            price, stops, node = heapq.heappop(queue)
            if node == dst:
                return price
            if stops>k or stops>stops_to_node[node]:
                continue
            stops_to_node[node]=stops
            for p, neighbor in adj[node]:
                heapq.heappush(queue,(p+price, stops+1, neighbor))
        return -1
