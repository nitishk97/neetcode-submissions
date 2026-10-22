class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        root = TrieNode()
        for w in wordDict:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_word = True
        
        dp = [False]*(n+1)
        dp[0] = True

        for i in range(n):
            if dp[i]:
                node = root
                curr_idx = i
                while curr_idx<n and s[curr_idx] in node.children:
                    node = node.children[s[curr_idx]]
                    curr_idx+=1
                    if node.is_word:
                        dp[curr_idx]=True
                    

        return dp[n]