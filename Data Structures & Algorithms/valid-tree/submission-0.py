class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()
        def hasCycle(node, parent):
            if node in visit:
                return True
            visit.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if hasCycle(neighbor, node):
                    return True
            return False
        return not hasCycle(0,-1) and len(visit)==n
        