class TrieNode:
    def __init__(self):
        self.children = {} # contains nodes of childrens
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]  # Always advance down the tree
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(idx, node):
            if idx==len(word):
                return node.endOfWord
            
            char = word[idx]
            if char==".":
                for child in node.children.values():
                    if dfs(idx+1, child):
                        return True
                return False
            if char in node.children:
                return dfs(idx+1, node.children[char])
            return False
        return dfs(0, self.root)
