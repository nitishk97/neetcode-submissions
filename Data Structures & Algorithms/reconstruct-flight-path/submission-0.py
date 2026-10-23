class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(reverse=True)
        for src, dst in tickets:
            adj[src].append(dst)
        result = []
        def dfs(node):
            while adj[node]:
                dst = adj[node].pop()
                dfs(dst)
            result.append(node)
        dfs("JFK")
        return result[::-1]
