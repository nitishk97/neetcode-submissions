class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        neighbors = [(-1,0),(0,1),(1,0),(0,-1)]
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c]=TrieNode()
                curr = curr.children[c]
            curr.word = word
        result = []
        def dfs(i,j,node):
            char = board[i][j]

            if char not in node.children:
                return
            
            nxt_node = node.children[char]
            board[i][j] = "#"
            if nxt_node.word:
                result.append(nxt_node.word)
                nxt_node.word = None

            for nr, nc in neighbors:
                row, col = nr+i, nc+j
                if 0<=row<len(board) and 0<=col<len(board[0]) and board[row][col] != "#":
                    dfs(row, col, nxt_node)
                
            board[i][j] = char
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c,root)
        return result

