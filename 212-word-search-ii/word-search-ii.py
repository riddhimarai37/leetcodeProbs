class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # implement a trie with list of words
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS = len(board)
        COLS = len(board[0])
        # res: words that we found in the board
        # visit: keeps track of characters come across in the run
        res, visit = set(), set()

        def dfs(r,c, node, word):
            # if we are out of bounds
            if (r < 0 or c < 0 
                or r == ROWS or c == COLS
                or (r,c) in visit or board[r][c] not in node.children):
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            # adding new char to word and seeing if its a word in the list
            word += board[r][c]
            if node.isWord:
                res.add(word)

            # adding chars in all directions to current word
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")

        return list(res)








        