class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        for w in words:
            node = root
            for char in w:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = w
            
        rows, cols = len(board), len(board[0])
        result = set()
        
        # Step 2: Define Backtracking / DFS function
        def dfs(r, c, node):
            char = board[r][c]
            # If character is not in current Trie node children, or cell is visited
            if char not in node.children:
                return
            
            next_node = node.children[char]
            if next_node.word:
                result.add(next_node.word)
                # Optimization: do not remove word immediately if you want to allow duplicates, 
                # but clearing it prevents finding the same word multiple times.
                # next_node.word = None 
            
            # Temporarily mark the current cell as visited
            board[r][c] = '#'
            
            # Explore all 4 adjacent directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)
                    
            # Restore the cell's original character
            board[r][c] = char
            
            # Optimization: prune leaf nodes to speed up future searches
            if not next_node.children:
                del node.children[char]

        # Step 3: Trigger DFS from every cell on the board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
                
        return list(result)