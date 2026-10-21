class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        if endWord not in wordList:
            return 0
        pattern_matching = {}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                if pattern not in pattern_matching:
                    pattern_matching[pattern] = []
                pattern_matching[pattern].append(word)
        queue = deque([(beginWord,1)])
        visited = set([beginWord])
        while queue:
            word, level = queue.popleft()
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                if pattern in pattern_matching:
                    for neigh in pattern_matching[pattern]:
                        if neigh == endWord:
                            return level+1
                        if neigh not in visited:
                            queue.append((neigh, level+1))
                            visited.add(neigh)
                pattern_matching[pattern] = []
        return 0

