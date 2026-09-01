from collections import deque
from typing import List

class Solution(object):
    def numIslands(self, grid: List[List[str]]) -> int:
        """:type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (
                        0 <= nr < rows 
                        and 0 <= nc < cols 
                        and grid[nr][nc] == "1" 
                        and (nr, nc) not in visited
                    ):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands