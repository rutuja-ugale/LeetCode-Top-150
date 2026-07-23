class Solution(object):
    def gameOfLife(self, board):
        
        m, n = len(board), len(board[0])
        
        # 8 possible directions for neighbors
        neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        for r in range(m):
            for c in range(n):
                live_count = 0
                
                # Count live neighbors
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        # Check if the neighbor was originally alive
                        if abs(board[nr][nc]) == 1:
                            live_count += 1
                
                # Apply Conway's rules using encoded states
                if board[r][c] == 1:
                    if live_count < 2 or live_count > 3:
                        board[r][c] = -1  # Live -> Dead
                else:
                    if live_count == 3:
                        board[r][c] = 2   # Dead -> Live
                        
        # Second pass to finalize the board to 0s and 1s
        for r in range(m):
            for c in range(n):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0