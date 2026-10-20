class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        parent = [i for i in range(n+1)]
        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        # detects cycle
        def union(u,v):
            root_u = find(u)
            root_v = find(v)
            if root_u==root_v:
                return True
            parent[root_u] = root_v
            return False
        for u, v in edges:
            if union(u,v):
                return [u,v]
        return []
