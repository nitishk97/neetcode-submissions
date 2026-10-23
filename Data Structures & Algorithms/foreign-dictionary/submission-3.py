class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adj = defaultdict(set)
        indegree = {c: 0 for w in words for c in w}
        for i in range(n-1):
            w1,w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1)>len(w2):
                if w1[:min_len]==w2[:min_len]:
                    return ""
            for j in range(min_len):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]]+=1
                    break
        queue = deque([char for char, count in indegree.items() if count == 0])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        if len(result)<len(indegree):
            return ""
        return "".join(result)
                

        
