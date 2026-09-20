class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # If we matched all characters in the word
            if i == len(word):
                return True
            
            # Check bounds, character match, and if already visited
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                word[i] != board[r][c] or 
                (r, c) in path):
                return False

            path.add((r, c))
            # Explore all 4 adjacent directions
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            # Backtrack
            path.remove((r, c))
            return res

        # Start DFS from every cell on the board
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
                    
        return False