from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        target = n * n

        def get_coordinates(square):
            r_bot = (square - 1) // n
            c_left = (square - 1) % n

            r = n - 1 - r_bot

            if r_bot % 2 == 1:
                c = n - 1 - c_left
            else:
                c = c_left

            return r, c

        queue = deque([(1, 0)])
        visited = {1}

        while queue:
            curr, moves = queue.popleft()

            if curr == target:
                return moves

            for next_square in range(
                curr + 1,
                min(curr + 6, target) + 1
            ):
                r, c = get_coordinates(next_square)

                if board[r][c] != -1:
                    destination = board[r][c]
                else:
                    destination = next_square

                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, moves + 1))

        return -1